# 💊 Meditab-AI - Medicine Analysis System

A Flask-based web application for analyzing medicine information through image uploads or text input.

🔗 **Live Demo**: [medilens-vision-guide.vercel.app](https://medilens-vision-guide.vercel.app/)

## ✨ Features

- 📸 Upload medicine images or enter medicine names
- 🔍 Get detailed medicine information
- 🎤 Text-to-speech for analysis results
- 📱 Responsive design with Tailwind CSS
- 🚀 Deployed on Vercel

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Deployment**: Vercel (Serverless)

## 🚀 Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Niyas-J/Meditab-AI.git
cd Meditab-AI
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

3. Run the Flask app:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 🌐 Deploy to Vercel

### Option 1: Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New Project"**
3. Import the repository: `Niyas-J/Meditab-AI`
4. Vercel will auto-detect the configuration
5. Click **"Deploy"**

### Option 2: Vercel CLI

```bash
npm install -g vercel
vercel login
vercel --prod
```

## 📁 Project Structure

```
Meditab-AI/
├── api/
│   └── index.py          # Vercel serverless entry point
├── templates/
│   ├── index.html        # Main page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   └── output.css        # Tailwind CSS
├── static/
│   └── images/          # Static images
├── app.py               # Flask app (for local development)
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Configuration

The app uses Flask with the following configuration:

- **Template folder**: `templates/`
- **Static folder**: `static/`
- **Max upload size**: 16MB
- **Host**: `0.0.0.0` (for Vercel compatibility)

## 📝 API Endpoints

- `GET /` - Main page
- `GET /why-us` - About page
- `GET /contact` - Contact page
- `POST /analyze` - Analyze medicine (accepts image upload or medicine name)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Niyas-J**

- GitHub: [@Niyas-J](https://github.com/Niyas-J)
- Repository: [Meditab-AI](https://github.com/Niyas-J/Meditab-AI)

## 🙏 Acknowledgments

- Built with Flask
- Styled with Tailwind CSS
- Deployed on Vercel

---

Made with ❤️ by Niyas-J
