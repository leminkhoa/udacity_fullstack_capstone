import unittest
import json
import os

from unittest.mock import patch
from flask_sqlalchemy import SQLAlchemy
from money_app import create_app

from models.respond_schema import *
from models.request_schema import *
from models.models import setup_db, Category, Transaction

TEST_DB_NAME = 'budget_db_test'


class MoneyAppTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        # Define test db name and reset
        os.environ['DB_NAME'] = TEST_DB_NAME
        # Create app for testing
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

    
    def tearDown(self):
        """Executed after reach test"""
        pass


    # ~~~~~~~~~~~~~ GET METHOD ~~~~~~~~~~~~~~~~~

    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_get_categories_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
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


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_get_categories_expect_404(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test get categories - Expect return status code 404
        """

        # setup mock
        mock_query\
            .return_value.filter\
            .return_value.one_or_none\
            .return_value = []
        
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_get_transactions_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test get transactions - Expect return status code 200
        """

        res = self.client().get('/transactions')
        data = json.loads(res.data)
        schema = GetTransactionRespondSchema()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(schema.validate(data), {})
        self.assertLessEqual(len(data['transactions']), 5) # Limit by pagination
        self.assertTrue(data['total_transactions'])


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_get_transactions_pagination_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test get transactions - Expect return status code 200
        """

        res = self.client().get('/transactions?page=2')
        data = json.loads(res.data)
        schema = GetTransactionRespondSchema()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(schema.validate(data), {})
        self.assertTrue(data['transactions'])
        self.assertTrue(data['total_transactions'])


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_get_transactions_expect_404(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test get transactions - Expect return status code 404
        """

        # setup mock
        mock_query\
            .return_value.filter\
            .return_value.one_or_none\
            .return_value = []
        
        res = self.client().get('/transactions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    # ~~~~~~~~~~~~~ POST METHOD ~~~~~~~~~~~~~~~~~

    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_category_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create category - Expect return status code 200
        """
        
        request_valid = {
                "transaction_type_id": "1",
                "type": "Utilities"                
            }

        res = self.client().post(
            '/categories', 
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_categories'])


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_category_expect_400_missing_field(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create category with missing
        field(s) - Expect return status code 400
        """
        
        request_missing_field = {
            'transaction_type_id': 'test_id',
        }

        res = self.client().post(
            '/categories', 
            json=request_missing_field
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_category_expect_400_wrong_datatype(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create category with wrong 
        datatype - Expect return status code 400
        """
        
        request_wrong_datatype = {
            'transaction_type_id': 1,
        }

        res = self.client().post(
            '/categories', 
            json=request_wrong_datatype
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_category_expect_422(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create category with non-exist 
        transaction_type_id - Expect return status code 422
        """

        request_integrity_error = {
            "transaction_type_id": "3",
            "type": "Utilities",               
        }

        res = self.client().post(
            '/categories', 
            json=request_integrity_error
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Category, "insert")
    def test_create_category_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create question - Expect return status code 500
        """

        # setup mock
        mock_query\
            .side_effect = Exception("test exception")   
        
        request_valid = {
                "transaction_type_id": "1",
                "type": "Utilities"                
            }

        res = self.client().post(
            f'/categories',
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_transaction_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create transaction - Expect return status code 200
        """
        
        request_valid = {
            "category_id": "1",
            "date": "2022-03-03T15:00:00Z",
            "amount": 7,
            "currency": "$",
            "note": "dummy note",
        }

        res = self.client().post(
            '/transactions', 
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_transaction_expect_400_missing_field(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create trasaction with missing
        field(s) - Expect return status code 400
        """
        
        request_missing_field = {
            # "category_id": "1",
            "date": "2022-03-03T15:00:00Z",
            # "amount": 7,
            "currency": "$",
            # "note": "dummy note",
        }

        res = self.client().post(
            '/transactions', 
            json=request_missing_field
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_transaction_expect_400_wrong_datatype(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create trasaction with wrong
        datatype - Expect return status code 400
        """
        
        request_missing_field = {
            "category_id": "1",
            "date": 100, # invalid date
            "amount": 7,
            "currency": "$",
        }

        res = self.client().post(
            '/transactions', 
            json=request_missing_field
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_create_transaction_expect_422(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create transaction with non-exist 
        category_id - Expect return status code 422
        """

        request_integrity_error = {
            "category_id": "100",
            "date": "2022-03-03T15:00:00Z",
            "amount": 7,
            "currency": "$",
            "note": "dummy note",
        }

        res = self.client().post(
            '/transactions', 
            json=request_integrity_error
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Transaction, "insert")
    def test_create_transaction_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test create question - Expect return status code 500
        """

        # setup mock
        mock_query\
            .side_effect = Exception("test exception")
        
        
        request_valid = {
            "category_id": "1",
            "date": "2022-03-03T15:00:00Z",
            "amount": 7,
            "currency": "$",
            "note": "dummy note",
        }


        res = self.client().post(
            f'/transactions',
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')


    # ~~~~~~~~~~~~~ UPDATE METHOD ~~~~~~~~~~~~~~~~~
   
    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_category_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update category - Expect return status code 200
        """
        
        request_valid = {
            "transaction_type_id": "1",
            "type": "Rent",
        }

        res = self.client().patch(
            '/categories/1', 
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['category'], 
            {
                "id": "1",
                "transaction_type_id": "1",
                "type": "Rent",  
            }
        )

    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_category_expect_400(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update category - Expect return status code 400
        """
        
        request_invalid = {
            "transaction_type_id": 100,
            "type": "Rent",
        }

        res = self.client().patch(
            '/categories/1', 
            json=request_invalid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_category_expect_404(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update category for non-exist 
        transaction_type_id - Expect return status code 404
        """
        
        request_valid = {
            "transaction_type_id": "1",
            "type": "Rent",
        }

        res = self.client().patch(
            '/categories/100',  # non-exist id
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Category, "update")
    def test_update_category_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update category with assumed error - Expect return status code 500
        """
        # setup mock
        mock_query\
            .side_effect = Exception("test exception")
        
        request_valid = {
            "transaction_type_id": "1",
            "type": "Rent",
        }

        res = self.client().patch(
            '/categories/1',  
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_transaction_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update transaction - Expect return status code 200
        """
        
        request_valid = {
            "category_id": "5",
            "date": "2022-03-03T15:00:00Z",
            "amount": 550,
            "currency": "$",
            "note": "updated note",
        }

        res = self.client().patch(
            '/transactions/2', 
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_transaction_expect_400(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update transaction - Expect return status code 400
        """
        
        request_invalid = {
            "category_id": "5",
            # "date": "2022-03-03T15:00:00Z",
            "amount": 550,
            # "currency": "$",
            "note": "updated note",
        }

        res = self.client().patch(
            '/transactions/1', 
            json=request_invalid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_update_transaction_expect_404(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update transaction for non-exist 
        transaction_type_id - Expect return status code 404
        """
        
        request_valid = {
            "category_id": "5",
            "date": "2022-03-03T15:00:00Z",
            "amount": 550,
            "currency": "$",
            "note": "updated note",
        }

        res = self.client().patch(
            '/transactions/100',  # non-exist id
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Transaction, "update")
    def test_update_transaction_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test update transaction with assumed error - Expect return status code 500
        """
        # setup mock
        mock_query\
            .side_effect = Exception("test exception")
        
        request_valid = {
            "category_id": "5",
            "date": "2022-03-03T15:00:00Z",
            "amount": 550,
            "currency": "$",
            "note": "updated note",
        }

        res = self.client().patch(
            '/transactions/1',  
            json=request_valid
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')


    # ~~~~~~~~~~~~~ DELETE METHOD ~~~~~~~~~~~~~~~~~

    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_delete_category_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete category - Expect return status code 200
        """

        res = self.client().delete(
            '/categories/2', 
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_delete_category_expect_404(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete category for non-exist category - Expect return status code 404
        """

        res = self.client().delete(
            '/categories/100', # non-exist category id
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Category, "delete")
    def test_delete_category_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete category with assumed exception - Expect return status code 500
        """
        
        # setup mock
        mock_query\
            .side_effect = Exception("test exception")

        res = self.client().delete(
            '/categories/3',
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_delete_transaction_expect_200(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete category - Expect return status code 200
        """

        res = self.client().delete(
            '/transactions/4', 
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    def test_delete_transaction_expect_404(self, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete category for non-exist category - Expect return status code 404
        """

        res = self.client().delete(
            '/transactions/100', # non-exist category id
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


    @patch('auth.check_permissions')
    @patch('auth.get_token_auth_header')
    @patch('auth.verify_decode_jwt')
    @patch.object(Transaction, "delete")
    def test_delete_transaction_expect_500(self, mock_query, mock_jwt, mock_get_token, mock_check_permissions):
        """
        Test delete transaction with assumed exception - Expect return status code 500
        """
        
        # setup mock
        mock_query\
            .side_effect = Exception("test exception")

        res = self.client().delete(
            '/transactions/3',
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')
