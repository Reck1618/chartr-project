from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteAPITestCase(APITestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title="Test Note 1", body="This is the body of test note 1.")
        self.note2 = Note.objects.create(title="Test Note 2", body="This is the body of test note 2.")
        self.note3 = Note.objects.create(title="Another Note", body="This is the body of another note.")

    def test_list_notes(self):
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Assuming 3 notes are created in setUp()

    def test_retrieve_note(self):
        url = reverse('note-detail', args=[self.note1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note1.title)

    def test_create_note(self):
        url = reverse('note-list')
        data = {'title': 'New Note', 'body': 'This is the body of the new note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 4)  # Assuming 4 notes are created after the new note is created

    def test_update_note(self):
        url = reverse('note-detail', args=[self.note1.pk])
        data = {'title': 'Updated Note', 'body': 'This is the updated body of the note.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note1.refresh_from_db()
        self.assertEqual(self.note1.title, 'Updated Note')

    def test_delete_note(self):
        url = reverse('note-detail', args=[self.note1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Note.objects.filter(pk=self.note1.pk).exists())
