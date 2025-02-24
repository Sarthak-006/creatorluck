# CreatorLuck 🎲

A decentralized gaming platform built on Creator Network for the Creator Hackathon 2025. Experience premium DeFi gaming with instant payouts and verifiable fairness.

## Features

- **DeFi Integration**
  - Built on Creator Network
  - CREATOR token integration
  - Smart contract-based gameplay
  - Verifiable random numbers

- **Game Types**
  1. Royal Single (10x payout)
  2. Golden Jodi (90x payout)
  3. Triple Crown (150x payout)
  4. Double Fortune (300x payout)
  5. Royal Flush (500x payout + Jackpot)

- **Premium Features**
  - Progressive jackpot system
  - Win streak bonuses
  - Achievement system
  - Real-time analytics
  - Mobile-responsive design

## Live Demo
Visit [CreatorLuck on Streamlit Cloud](https://creatorluck.streamlit.app)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/creatorluck.git
cd creatorluck
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

## Deployment

### GitHub
1. Create a new repository on GitHub
2. Initialize git and push code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/creatorluck.git
git push -u origin main
```

### Streamlit Cloud
1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and branch
5. Click "Deploy!"

## Project Structure
```
creatorluck/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
├── .streamlit/           # Streamlit configuration
│   └── config.toml       # Streamlit settings
├── static/               # Static assets
│   └── css/             
│       └── style.css     # Custom styling
└── utils/               # Utility modules
    ├── game_logic.py    # Game mechanics
    └── ui_components.py # UI components
```

## Contributing
This project is part of the Creator Hackathon 2025. Feel free to submit issues and enhancement requests.

## License
MIT License

## Acknowledgments
- Creator Network team
- Streamlit team
- Creator Hackathon organizers 