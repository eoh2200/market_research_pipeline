**example usage**:

`python main.py --use_case "residential decking" --end_user "homeowners" --purchaser "homeowners/building contractors" --geo "Midwest"`

**Output**: `output_prompts` directory will be created and populated with .txt files that can be copied and pasted directly into LLM one at a time.
 



- `use_case`, `end_user`, and `purchaser` are required. 
- if not specified, `geo` defaults to "United States".