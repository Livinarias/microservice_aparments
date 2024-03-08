import unittest
from unittest.mock import MagicMock
# from your_module import call_data

class TestDataHelper(unittest.TestCase):
    def test_call_data_with_valid_path(self):
        # Arrange
        path = "/path/to/data"
        expected_data = [
            {
                "Dirección": "123 Main St",
                "Ciudad": "City",
                "Estado": "State",
                "Precio de venta": 100000,
                "Descripción": "Lorem ipsum"
            },
            {
                "Dirección": "456 Elm St",
                "Ciudad": "City",
                "Estado": "State",
                "Precio de venta": 200000,
                "Descripción": "Lorem ipsum"
            }
        ]
        mock_service = MagicMock()
        mock_service.get_data.return_value = [
            ("123 Main St", "City", "State", 100000, "Lorem ipsum"),
            ("456 Elm St", "City", "State", 200000, "Lorem ipsum")
        ]

        # Act
        # result = call_data(path)

        # # Assert
        # self.assertEqual(result, expected_data)
        mock_service.get_data.assert_called_once_with(path)

    def test_call_data_with_invalid_path(self):
        # Arrange
        # path = "/path/to/data?year=2022"
        # expected_error = CreatorSplitError()
        mock_service = MagicMock()
        mock_service.get_data.return_value = []

        # Act
        # result = call_data(path)

        # Assert
        # self.assertEqual(result, expected_error)
        mock_service.get_data.assert_not_called()

if __name__ == '__main__':
    unittest.main()