import json
import os

def load_lesson_data(file_path: str) -> dict:
    """
    Loads lesson data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
        
    Returns:
        dict: The loaded data.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    return data

def get_all_lessons(data_dir: str) -> list:
    """
    Scans the data directory for lesson JSON files and returns a list of summaries.
    
    Args:
        data_dir (str): Path to the directory containing JSON files.
        
    Returns:
        list: A list of dicts containing 'id', 'title', and 'file_name'.
    """
    lessons = []
    if not os.path.exists(data_dir):
        return lessons

    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            try:
                # We only need the header info, but loading the whole file is fine for this scale
                data = load_lesson_data(file_path)
                lessons.append({
                    "id": data.get("lesson_id"),
                    "title": data.get("title"),
                    "file_name": filename
                })
            except Exception as e:
                print(f"Skipping {filename}: {e}")
                
    # Sort by ID
    lessons.sort(key=lambda x: x["id"])
    return lessons

def get_lesson_by_id(lesson_id: int, data_dir: str) -> dict:
    """
    Finds and loads a lesson by its ID.
    
    Args:
        lesson_id (int): The lesson ID to find.
        data_dir (str): Path to the directory containing JSON files.
        
    Returns:
        dict: The lesson data.
        
    Raises:
        FileNotFoundError: If the lesson ID is not found.
    """
    # In a real app, we might check file naming convention or scan all. 
    # For now, let's scan all to be safe since filenames might vary.
    all_lessons = get_all_lessons(data_dir)
    for lesson in all_lessons:
        if lesson["id"] == lesson_id:
            return load_lesson_data(os.path.join(data_dir, lesson["file_name"]))
            
    raise FileNotFoundError(f"Lesson with ID {lesson_id} not found.")

