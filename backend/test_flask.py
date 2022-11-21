import unittest
import json

from unittest.mock import patch
from flask_sqlalchemy import SQLAlchemy
from money_app import create_app

from models.respond_schema import *
from models.request_schema import *
from models.models import setup_db, Category


class MoneyAppTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "budget_db_test"
        self.database_path = 'postgresql://{}/{}'.format('postgres:abc@localhost:5432', self.database_name)
        setup_db(self.app)

        self.new_question = {
            'question': 'test_question',
            'answer': 'test_answer',
            'category': 3,
            'difficulty': 5,
        }

        self.search_question = {
            'searchTerm': 'what'
        }

        self.quizzes = {
            'quiz_category': {
                'id': 5
            },
            'previous_questions': [2, 4, 6]
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_categories_expect_200(self):
        """
        Test get categories - Expect return status code 200
        """

        res = self.client().get('/categories')
        data = json.loads(res.data)
        schema = GetCategoryRespondSchema()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(schema.validate(data), {})
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))


    # @patch('flask_sqlalchemy._QueryProperty.__get__')
    # def test_get_categories_expect_404(self, mock_query):
    #     """
    #     Test get categories - Expect return status code 404
    #     """

    #     # setup mock
    #     mock_query\
    #         .return_value.filter\
    #         .return_value.one_or_none\
    #         .return_value = []
        
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['error'], 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not Found')


    #     # binds the app to the current context
    #     with self.app.app_context():
    #         self.db = SQLAlchemy()
    #         self.db.init_app(self.app)
    #         # create all tables
    #         self.db.create_all()