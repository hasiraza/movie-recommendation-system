# 🎬 Movie Recommendation System

A sleek and modern movie recommendation system built with Streamlit that suggests similar movies based on your selection. Features an elegant glassmorphism UI with blur effects and enhanced visual styling.


## ✨ Features

- **Content-Based Filtering**: Recommends movies similar to your selected movie
- **Beautiful UI**: Modern glassmorphism design with blur effects
- **Movie Posters**: High-quality movie posters fetched from TMDB API
- **Interactive Interface**: Easy-to-use dropdown selection and recommendation display
- **Responsive Design**: Clean layout that works across different screen sizes

## 🚀 Demo

The system displays:
- A dropdown menu to select movies from the trained dataset
- 5 similar movie recommendations with posters
- Blurred background effect for enhanced visual appeal
- Movie titles with styled backgrounds

## 📋 Prerequisites

Before running the application, make sure you have the following installed:

```bash
pip install streamlit
pip install requests
pip install pickle
```

## 🛠️ Installation & Setup

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd movie-recommendation-system
   ```

2. **Required Files Structure**
   ```
   project-folder/
   ├── app.py                    # Main application file
   ├── background.jpg            # Background image
   ├── Models/
   │   ├── movies_list.pkl       # Preprocessed movie data
   │   └── similarty.pkl         # Similarity matrix
   └── README.md
   ```

3. **Add Background Image**
   - Place a `background.jpg` file in the root directory
   - This will be used as the background for the application

4. **Model Files**
   - Ensure you have the trained model files in the `Models/` folder:
     - `movies_list.pkl`: Contains movie data with titles and IDs
     - `similarty.pkl`: Contains the similarity matrix for recommendations

## 🎯 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`

3. **Get Recommendations**
   - Select a movie from the dropdown menu
   - Click "🎯 Show Recommendations"
   - View 5 similar movie recommendations with posters

## 🎨 UI Features

### Design Elements
- **Glassmorphism Effect**: Modern blur effects throughout the interface
- **Dark Theme**: Elegant dark background with transparency
- **Enhanced Posters**: Large movie posters (250px width) with hover effects
- **Styled Dropdowns**: Black-themed dropdown with white text
- **Blur Recommendation Area**: Special blur container for movie suggestions

### Color Scheme
- Background: Dark overlay with custom background image
- Primary: Orange/Red buttons (`rgba(255, 87, 51, 0.8)`)
- Text: White with shadow effects
- Containers: Semi-transparent with blur effects

## 🔧 Technical Details

### API Integration
- **TMDB API**: Fetches movie posters using The Movie Database API
- **API Key**: Configured for movie poster retrieval
- **Image URLs**: Uses TMDB's image service for high-quality posters

### Recommendation Algorithm
- **Content-Based Filtering**: Uses movie similarity matrix
- **Cosine Similarity**: Calculates similarity between movies
- **Top 5 Results**: Returns the most similar movies

### File Dependencies
```python
import streamlit as st
import pickle
import requests
import base64
```

## 📂 File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `background.jpg` | Background image for the UI |
| `Models/movies_list.pkl` | Preprocessed movie dataset |
| `Models/similarty.pkl` | Similarity matrix for recommendations |

## 🎭 How It Works

1. **Movie Selection**: User selects a movie from the dropdown
2. **Similarity Calculation**: System finds the movie in the dataset
3. **Recommendation Generation**: Uses similarity matrix to find top 5 similar movies
4. **Poster Fetching**: Retrieves movie posters from TMDB API
5. **Display Results**: Shows recommendations in a beautiful blurred container

## 🚨 Important Notes

- The system only recommends movies that exist in the training dataset
- If you select a movie not in the dataset, no recommendations will be shown
- Internet connection is required for fetching movie posters
- Background image (`background.jpg`) is optional but recommended for best visual experience

## 🤝 Contributing

Feel free to contribute to this project! You can:
- Report bugs and issues
- Suggest new features
- Improve the UI/UX
- Optimize the recommendation algorithm

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **TMDB API** for providing movie poster data
- **Streamlit** for the amazing web framework
- **Scikit-learn** for machine learning utilities used in preprocessing

---

**Developed by:** Muhammad Haseeb Raza  
**Contact:** hasiraza511@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/  
**GitHub:** https://github.com/hasiraza