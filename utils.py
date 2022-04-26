import json

def load_candidates_from_json(url):
    """ Возвращает список всех кандидатов"""
    with open(url, 'r', encoding='utf-8') as candidates:  # открывает файл для чтения
        return json.load(candidates)

def get_candidate(candidate_id):
    """ Возвращает кандидата по номеру"""
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name):
    """ Возвращает кандидата по имени"""
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            matches.append(candidate)
    return matches

def get_candidates_by_skill(skill_name):
    """ Возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            matches.append(candidate)
    return matches



