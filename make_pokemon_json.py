import json

inputpath = 'data/2026-03-gen9championsvgc2026regma-0.json'
outputpath = inputpath.replace('data', 'processed_data')

with open(inputpath) as f:
    raw_data = json.load(f)

processed_data = {}
total_usage = {}

# Pre-calculate usage and teammate frequencies
for pokemon, details in raw_data['data'].items():
    teammates = details.get('Teammates', {})
    
    # Calculate this Pokemon's total games (Sum of teammates / 5)
    games_played = sum(teammates.values()) / 5 if teammates else 1
    total_usage[pokemon] = games_played
    
    processed_data[pokemon] = {
        "usage": games_played,
        "teammates": teammates
    }

# Save for the web
output = {
    "pokemon": processed_data,
    "total_usage": total_usage
}
with open(outputpath, 'w') as f:
    json.dump(output, f)