import unittest
from agenda import Agenda 

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("Meeting", "2024-07-16", "Discuss project status")
        self.assertEqual(len(self.agenda.events), 1)
        self.assertEqual(self.agenda.events[0].title, "Meeting")
        self.assertEqual(self.agenda.events[0].date, "2024-07-16")
        self.assertEqual(self.agenda.events[0].description, "Discuss project status")

    def test_remove_event(self):
        self.agenda.add_event("Meeting", "2024-07-16", "Discuss project status")
        self.agenda.remove_event("Meeting")
        self.assertEqual(len(self.agenda.events), 0)

    def test_list_events(self):
        self.agenda.add_event("Meeting", "2024-07-16", "Discuss project status")
        self.agenda.add_event("Workshop", "2024-07-17", "Python workshop")
        events_list = [str(event) for event in self.agenda.events]
        self.assertIn("Title: Meeting, Date: 2024-07-16, Description: Discuss project status", events_list)
        self.assertIn("Title: Workshop, Date: 2024-07-17, Description: Python workshop", events_list)

if __name__ == "__main__":
    unittest.main()

