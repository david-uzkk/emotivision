import pandas as pd
import numpy as np
import json
from pathlib import Path
from collections import defaultdict

def load_results(json_path):
    """
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    print(f'📂 Loaded{len(results)} results of: {json_path}')

    return results

