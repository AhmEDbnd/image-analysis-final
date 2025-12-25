# Project 1: Histogram Analysis and Manipulation

## 📸 Digital Photography

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-latest-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-red.svg)

---

## 📋 Project Description

This project explores the analysis and manipulation of grayscale image histograms, with a specific application to **digital photography**. The goal is to understand how to enhance image contrast using different histogram equalization techniques.

### 🎯 Objectives

- Calculate and analyze an image histogram
- Understand the role of the cumulative histogram
- Apply global histogram equalization
- Use the CLAHE (Contrast Limited Adaptive Histogram Equalization) method
- Compare results and evaluate enhancement quality

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **OpenCV**: Image processing
- **NumPy**: Numerical computations
- **Matplotlib**: Results visualization

---

## 📦 Installation

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### Installing Dependencies

```bash
pip install opencv-python numpy matplotlib
```

Or use the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```
opencv-python>=4.5.0
numpy>=1.19.0
matplotlib>=3.3.0
```

---

## 🚀 Usage

### Option 1: Use the Sample Image

Simply run the script:

```bash
python project1_histograms.py
```

The script automatically generates a sample image for demonstration.

### Option 2: Use Your Own Image

1. Place your image in the same folder as the script
2. Modify the code:

```python
# Comment this line:
# image = create_sample_image()

# Uncomment and modify this line:
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)
```

3. Run the script:

```bash
python project1_histograms.py
```

---

## 📊 Generated Results

The script automatically generates:

### 1. **Complete Figure** (`project1_results.png`)
   - Images: Original, Equalized, CLAHE
   - Histograms of all three versions
   - Cumulative histogram
   - Dynamic range comparison graph

### 2. **Text Analysis** (console)
   - Manual histogram calculation
   - Verification with OpenCV
   - Dynamic range calculations (min/max)
   - Comparative method analysis

---

## 📖 Code Structure

```
project1_histograms.py
│
├── create_sample_image()          # Create sample image
├── calcul_histogramme_manuel()    # Manual calculation with loops
├── OpenCV histogram calculation   # Verification
├── Cumulative histogram           # Cumulative analysis
├── Global equalization            # cv2.equalizeHist()
├── CLAHE                          # Adaptive equalization
├── calculer_dynamique()           # Min, max, dynamic range
└── Complete visualization         # Matplotlib
```

---

## 🔍 Technical Explanations

### 1. **Histogram**
The histogram represents the distribution of gray levels in an image (0-255). It allows analysis of:
- Intensity distribution
- Global contrast
- Underexposed or overexposed areas

### 2. **Cumulative Histogram**
Cumulative sum of the histogram. Used for:
- Understanding cumulative distribution
- Mathematical basis of equalization

### 3. **Global Equalization**
```python
image_equalized = cv2.equalizeHist(image)
```
- Uniformly redistributes intensities
- Improves global contrast
- May over-amplify noise

### 4. **CLAHE (Contrast Limited Adaptive Histogram Equalization)**
```python
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(image)
```
- **clipLimit**: Limits contrast to avoid over-amplification
- **tileGridSize**: Tile size for local equalization
- Better preserves local details

### 5. **Dynamic Range**
```
Dynamic Range = max(image) - min(image)
```
Measures the extent of intensities used (0-255 = maximum dynamic range)

---

## 📈 Expected Results

### Original Image
- Histogram concentrated in certain areas
- Limited contrast
- Variable dynamic range

### Equalized Image
- Uniform distribution over [0-255]
- Maximum contrast
- Dynamic range = 255
- May create artifacts

### CLAHE Image
- Balanced distribution
- Locally enhanced contrast
- Dynamic range = 255
- More natural appearance

---

## 📝 Sample Results

### Typical values obtained:

| Method | Min | Max | Dynamic Range | Quality |
|---------|-----|-----|-----------|---------|
| Original | 0 | 243 | 243 | Low contrast |
| Equalized | 0 | 255 | 255 | High contrast |
| CLAHE | 0 | 255 | 255 | Optimal |

---

## 🎓 Required Tasks (according to PDF)

- [x] Load a grayscale image
- [x] Calculate histogram manually (loops)
- [x] Verify with cv2.calcHist
- [x] Plot cumulative histogram and interpret
- [x] Apply global equalization: equalizeHist
- [x] Apply CLAHE: explain its benefits
- [x] Compare original, equalized, and CLAHE images
- [x] Calculate dynamic range (min/max) before and after

---

## 📄 Deliverables

### To submit:

1. **Figure**: `project1_results.png`
   - Original image + enhanced versions
   - Histograms

2. **Analysis**: 8-10 line text (provided in code)

3. **Report**: PDF document containing:
   - Introduction
   - Methodology
   - Results (figures)
   - Analysis and interpretation
   - Conclusion

---

## 💡 Results Interpretation

### Why CLAHE is better for photography?

1. **Preserves Local Details**
   - Adaptive processing by regions
   - No information loss in homogeneous areas

2. **Natural Contrast**
   - Avoids over-saturation
   - More pleasing visual rendering

3. **Noise Limitation**
   - The `clipLimit` parameter controls amplification
   - Reduces artifacts in uniform areas

4. **Flexibility**
   - Adjustable parameters (clipLimit, tileGridSize)
   - Adaptable to different image types

---

## 🔧 Customization

### Modify CLAHE parameters:

```python
# Increase contrast
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))

# Finer processing
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))

# More global processing
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(4, 4))
```

### Test different images:

```python
# Portrait
image = cv2.imread('portrait.jpg', cv2.IMREAD_GRAYSCALE)

# Landscape
image = cv2.imread('landscape.jpg', cv2.IMREAD_GRAYSCALE)

# Night photo
image = cv2.imread('night.jpg', cv2.IMREAD_GRAYSCALE)
```

---

## 🐛 Troubleshooting

### Problem: Image too dark after processing
**Solution**: Adjust CLAHE's `clipLimit` (increase to 3.0 or 4.0)

### Problem: Visible artifacts
**Solution**: Increase `tileGridSize` to (16, 16) or (32, 32)

### Problem: Image reading error
**Solution**: Check file path and format (JPG, PNG supported)

### Problem: Manual histogram ≠ OpenCV
**Solution**: Check data types (uint8) and bounds [0, 255]

---

## 📚 References

1. **OpenCV Documentation**
   - [Histogram Equalization](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)
   - [CLAHE](https://docs.opencv.org/4.x/d6/dc7/group__imgproc__hist.html#gad689d2607b7b3889453804f414ab1018)

2. **Scientific Papers**
   - Zuiderveld, K. (1994). "Contrast Limited Adaptive Histogram Equalization"
   - Pizer, S. M. et al. (1987). "Adaptive histogram equalization"

3. **M1 STIC Course**
   - Dr. HALLACI S. - Projects 2025

---

## 👨‍💻 Author

**Project completed as part of:**
- **M1 STIC** - Image Processing
- **Instructor**: Dr. HALLACI S
- **Year**: 2025

---

## 📧 Contact

For any questions about this project:
- Instructor email: [to be completed]
- OpenCV Documentation: https://docs.opencv.org/

---

## 📜 License

This project is completed in an educational context.


---

## 🌟 Possible Improvements

To go further:

1. **Quality Metrics**
   - Calculate PSNR (Peak Signal-to-Noise Ratio)
   - Calculate SSIM (Structural Similarity Index)

2. **Graphical Interface**
   - Create interface with Tkinter
   - Adjust parameters in real-time

3. **Extended Comparison**
   - Test on multiple image types
   - Create automatic comparison table

4. **Optimization**
   - Parallelize manual calculation
   - Use vectorized NumPy

---


*Last updated: December 2025*