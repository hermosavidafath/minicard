#!/bin/bash
# Quick Deploy Script untuk Linux/Mac

echo "🚀 Rentry Quick Deploy"
echo "======================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

echo "Choose deployment platform:"
echo "1. Heroku"
echo "2. Railway" 
echo "3. Render"
echo "4. Docker"
echo "5. Manual setup info"

read -p "Enter choice (1-5): " choice

case $choice in
    1)
        echo "🔧 Setting up Heroku deployment..."
        if ! command -v heroku &> /dev/null; then
            echo "❌ Heroku CLI not installed. Install from: https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        read -p "Enter app name: " app_name
        heroku create $app_name
        heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
        heroku config:set FLASK_ENV=production
        
        echo "✅ Heroku app created. Deploy with:"
        echo "git push heroku main"
        ;;
        
    2)
        echo "🔧 Setting up Railway deployment..."
        if ! command -v railway &> /dev/null; then
            echo "Installing Railway CLI..."
            npm install -g @railway/cli
        fi
        
        echo "✅ Railway setup. Deploy with:"
        echo "railway login"
        echo "railway up"
        ;;
        
    3)
        echo "🔧 Render deployment info:"
        echo "1. Push code to GitHub"
        echo "2. Connect repository to Render"
        echo "3. Set build command: pip install -r requirements.txt"
        echo "4. Set start command: gunicorn wsgi:application"
        echo "5. Add environment variables"
        ;;
        
    4)
        echo "🔧 Building Docker image..."
        docker build -t rentry-app .
        echo "✅ Docker image built. Run with:"
        echo "docker run -p 5000:5000 -e SECRET_KEY=your-secret-key rentry-app"
        ;;
        
    5)
        echo "📋 Manual deployment checklist:"
        echo "1. Set environment variables:"
        echo "   SECRET_KEY=your-secret-key"
        echo "   FLASK_ENV=production"
        echo "   DATABASE_URL=your-database-url"
        echo ""
        echo "2. Install dependencies:"
        echo "   pip install -r requirements.txt"
        echo ""
        echo "3. Initialize database:"
        echo "   python db_manager.py init"
        echo ""
        echo "4. Run with gunicorn:"
        echo "   gunicorn wsgi:application"
        ;;
        
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Setup complete! Check DEPLOYMENT.md for detailed instructions."