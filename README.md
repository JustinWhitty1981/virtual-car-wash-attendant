# 🚗 Virtual Car Wash Attendant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An AI-powered vehicle safety and compatibility assessment system for automated car wash facilities.

![Car Wash System Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Virtual+Car+Wash+Attendant)

## 🌟 Features

### 🤖 AI-Powered Analysis
- **GPT-4o Vision Integration**: Advanced multimodal AI analyzes vehicle images for safety assessment
- **Smart Decision Making**: Automatically determines if vehicles are suitable for car wash entry
- **Real-time Processing**: Instant analysis with detailed reasoning for each decision

### 🎨 Modern Web Interface
- **Professional Design**: Beautiful gradient UI with responsive layout
- **Real-time Status**: Live system monitoring with animated status indicators
- **Interactive Dashboard**: Intuitive controls for operators with smooth animations
- **Mobile Responsive**: Works seamlessly across all device sizes

### 🔧 Robust System Architecture
- **Camera Integration**: Supports live camera feeds with intelligent fallback to sample images
- **Manual Override**: Operator controls for decision overrides with audit logging
- **History Tracking**: Complete audit trail of all decisions and operator actions
- **Error Handling**: Graceful degradation and comprehensive error management

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Webcam (optional - system works with sample images)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JustinWhitty1981/virtual-car-wash-attendant.git
   cd virtual-car-wash-attendant
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv my_flask_env
   source my_flask_env/bin/activate  # On Windows: my_flask_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask openai python-dotenv opencv-python requests
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the web interface**
   Open your browser and navigate to `http://localhost:5000`

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │  Flask Backend  │    │   AI Analysis   │
│                 │◄──►│                 │◄──►│                 │
│  - Dashboard    │    │  - API Routes   │    │  - GPT-4o       │
│  - Controls     │    │  - Image Serve  │    │  - Vision API   │
│  - History      │    │  - Logging      │    │  - Decision AI  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         ▲                        ▲                        ▲
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Image Capture   │    │ Decision System │    │ Barrier Control │
│                 │    │                 │    │                 │
│ - Camera Feed   │    │ - Logic Engine  │    │ - Entry Control │
│ - Sample Images │    │ - Override Mgmt │    │ - Safety System │
│ - Fallback Sys  │    │ - Audit Trail   │    │ - Auto Close    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### File Structure

```
virtual-car-wash-attendant/
├── 📁 captured_images/          # Vehicle image storage
│   ├── vehicle_20250330_161543.jpg
│   └── vehicle_20250330_162116.jpg
├── 📁 templates/                # Web interface templates
│   └── index.html              # Main dashboard interface
├── 📁 my_flask_env/            # Python virtual environment
├── 📄 main.py                  # Flask application entry point
├── 📄 imagecapture.py          # Camera and image handling
├── 📄 mmllm.py                 # AI analysis integration
├── 📄 decision.py              # Decision logic and logging
├── 📄 barriercontrol.py        # Physical barrier control
├── 📄 .env                     # Environment configuration
├── 📄 .gitignore              # Git ignore rules
└── 📄 README.md               # This documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Camera Configuration
CAMERA_ID=0
CAMERA_WIDTH=1920
CAMERA_HEIGHT=1080

# Optional: Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
```

### AI Analysis Criteria

The system evaluates vehicles based on:

- **Size Compatibility**: Height and width restrictions
- **Vehicle Modifications**: Lifted trucks, oversized vehicles
- **Safety Concerns**: Loose parts, visible damage
- **Special Handling**: Convertibles with soft tops
- **Attachments**: Roof racks, bike carriers, cargo boxes

## 🎯 Usage

### Basic Operation

1. **Start the System**: Launch the Flask application
2. **Monitor Dashboard**: View real-time system status
3. **Capture & Analyze**: Click to process vehicle images
4. **Review Decisions**: Check AI analysis and recommendations
5. **Manual Override**: Use operator controls when needed
6. **Track History**: Monitor all decisions in the audit log

### Decision Types

| Decision | Description | Action |
|----------|-------------|---------|
| **ALLOW** | Vehicle is safe for car wash | ✅ Barrier opens automatically |
| **DENY** | Vehicle poses safety risks | ❌ Entry blocked |
| **REVIEW** | Manual inspection required | ⚠️ Operator decision needed |

### Manual Override Process

1. Enter **Operator ID** for accountability
2. Provide **Override Reason** for audit trail
3. Select **Allow Entry** or **Deny Entry**
4. System logs all override actions

## 🛠️ Development

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Testing

```bash
# Run basic functionality tests
python -m pytest tests/

# Test with sample images
python test_analysis.py

# Check API endpoints
curl -X POST http://localhost:5000/capture
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where appropriate

## 🔒 Security Considerations

- **API Key Protection**: Never commit API keys to version control
- **Input Validation**: All user inputs are sanitized
- **Audit Logging**: Complete trail of all system actions
- **Access Control**: Operator ID required for overrides

## 🚀 Deployment

### Production Setup

1. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 main:app
   ```

2. **Set up reverse proxy** (nginx recommended)
3. **Configure SSL/TLS** for secure connections
4. **Set up monitoring** and logging
5. **Regular backups** of decision logs

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

## 📊 Monitoring & Analytics

### System Metrics

- **Processing Time**: Average AI analysis duration
- **Decision Distribution**: ALLOW/DENY/REVIEW ratios
- **Override Frequency**: Manual intervention rates
- **System Uptime**: Availability monitoring

### Log Analysis

```bash
# View recent decisions
tail -f car_wash_entries.log

# Analyze decision patterns
grep "DENY" car_wash_entries.log | wc -l
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Set up development environment
3. Install pre-commit hooks
4. Run tests before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing the GPT-4o Vision API
- **Flask** community for the excellent web framework
- **Bootstrap** for the responsive UI components
- **Font Awesome** for the beautiful icons

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Multi-camera support
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] Cloud deployment options

### Version 2.1 (Future)
- [ ] Machine learning model training
- [ ] Integration with POS systems
- [ ] Advanced reporting features
- [ ] Multi-language support

---

<div align="center">

**Made with ❤️ by the Virtual Car Wash Team**

[⭐ Star this repo](https://github.com/JustinWhitty1981/virtual-car-wash-attendant) • [🐛 Report Bug](https://github.com/JustinWhitty1981/virtual-car-wash-attendant/issues) • [✨ Request Feature](https://github.com/JustinWhitty1981/virtual-car-wash-attendant/issues)

</div>
