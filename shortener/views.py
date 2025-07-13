from django.shortcuts import render
from django.http import HttpResponse  # ✅ Add this

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer
import string, random




# Helper function to generate random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def form_interface(request):
    context = {}

    if request.method == 'POST':
        action = request.POST.get('action')
        

        # 1. Shorten
        if action == 'shorten':
            url = request.POST.get('url')
            code = generate_short_code()
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            obj = ShortURL.objects.create(url=url, short_code=code)
            context['short_url'] = request.build_absolute_uri(f'/shorten/{obj.short_code}/')

        # 2. Get Original
        elif action == 'get':
            code = request.POST.get('code')
            try:
                obj = ShortURL.objects.get(short_code=code)
                obj.access_count += 1
                obj.save()
                context['original_url'] = obj.url
            except ShortURL.DoesNotExist:
                context['original_url'] = 'Not found.'

        # 3. Update
        elif action == 'update':
            code = request.POST.get('code')
            new_url = request.POST.get('url')
            try:
                obj = ShortURL.objects.get(short_code=code)
                obj.url = new_url
                obj.save()
                context['updated_url'] = obj.url
            except ShortURL.DoesNotExist:
                context['updated_url'] = 'Short code not found.'

        # 4. Delete
        elif action == 'delete':
            code = request.POST.get('code')
            try:
                obj = ShortURL.objects.get(short_code=code)
                obj.delete()
                context['deleted'] = code
            except ShortURL.DoesNotExist:
                context['deleted'] = 'Short code not found.'

        # 5. Stats
        elif action == 'stats':
            code = request.POST.get('code')
            try:
                obj = ShortURL.objects.get(short_code=code)
                context['stats'] = {'code': code, 'count': obj.access_count}
            except ShortURL.DoesNotExist:
                context['stats'] = {'code': code, 'count': 'Not found'}

    return render(request, 'index.html', context)




class CreateShortURL(APIView):
    def post(self, request):
        original_url = request.data.get('url')

        if not original_url:
            return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)

        short_code = generate_short_code()
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()

        short_url = ShortURL.objects.create(
            url=original_url,
            short_code=short_code
        )

        serializer = ShortURLSerializer(short_url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# ✅ Homepage view

class RetrieveOrignalURL(APIView):
    def get(self, request, code):
        try:
            entry = ShortURL.objects.get(short_code=code)
            entry.access_count += 1
            entry.save()
            
            serializer = ShortURLSerializer(entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShortURL.DoesNotExist:
            return Response({'error': 'Short URL not found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateShortURL(APIView):
    def put(self, request, code):
        try:
            entry = ShortURL.objects.get(short_code=code)
        except ShortURL.DoesNotExist:
            return Response({'error': 'Short URL not found'}, status=status.HTTP_404_NOT_FOUND)

        new_url = request.data.get('url')

        if not new_url:
            return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)

        entry.url = new_url
        entry.save()

        serializer = ShortURLSerializer(entry)
        return Response(serializer.data, status=status.HTTP_200_OK)



class DeleteShortURL(APIView):
    def delete(self, request, code):
        try:
            entry = ShortURL.objects.get(short_code=code)
            entry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShortURL.DoesNotExist:
            return Response({'error': 'Short URL not found'}, status=status.HTTP_404_NOT_FOUND)



class URLStats(APIView):
    def get(self, request, code):
        try:
            entry = ShortURL.objects.get(short_code=code)
            return Response({
                'short_code': entry.short_code,
                'access_count': entry.access_count
            }, status=status.HTTP_200_OK)
        except ShortURL.DoesNotExist:
            return Response({'error': 'Short URL not found'}, status=status.HTTP_404_NOT_FOUND)




def homepage(request):
    return HttpResponse("""
        <h1>Welcome to the URL Shortener API</h1>
        <p>Use <code>/shorten/</code> to create a short URL.</p>
    """)
