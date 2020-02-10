from django.test import TestCase
from . models import ToDoList
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(
            first_name = "Sonam" ,
            last_name = "Sherpa",
            username = "mrsonam",
            email = "sonam@gmail.com",
            password = "sonam123",
            
        )

        todolist1 = ToDoList.objects.create(
            item = "Go to school",
            user_id = user1
        )
        todolist2 = ToDoList.objects.create(
            item = "Go to mall",
            user_id = user1
        )
        todolist3 = ToDoList.objects.create(
            item = "Go to home",
            completed = True,
            user_id = user1
        )

    def test_count_list(self):
        lists = ToDoList.objects.filter(completed=False)
        value = lists.count()
        self.assertEquals(value,2)

    def test_delete_list(self):
        lists = ToDoList.objects.filter(completed=True)
        lists.delete()
        value = lists.count()
        self.assertEquals(value,0)


    
        