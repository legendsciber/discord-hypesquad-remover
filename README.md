# Discord HypeSquad Remover

A simple Python script to remove the HypeSquad badge from your Discord account.

## Usage

1. Open `main.py` and replace `"token"` with your Discord token.
2. Run the script:

```bash
python main.py
```

## How it works

The script sends a `DELETE` request to the Discord API endpoint `/hypesquad/online` with your authorization token to leave the HypeSquad program and remove the badge from your profile.

## Notes

- Your token is sensitive. Do not share it with anyone.
- Using self-bots or automating user accounts may violate Discord's Terms of Service. Use at your own risk.
