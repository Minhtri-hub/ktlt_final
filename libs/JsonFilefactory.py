import json
import os
from typing import Any, Dict, List, Optional


class JsonFileFactory:
    def __init__(self, data_dir: str):
        """Initialize the JsonFileFactory with a data directory path."""
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def write_json(self, data: List[Dict[str, Any]], filename: str) -> bool:
        """
        Write data to a JSON file.

        Args:
            data: List of dictionaries to write
            filename: Name of the JSON file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return False

    def read_json(self, filename: str) -> Optional[List[Dict[str, Any]]]:
        """
        Read data from a JSON file.

        Args:
            filename: Name of the JSON file

        Returns:
            Optional[List[Dict[str, Any]]]: List of dictionaries if successful, None otherwise
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None

