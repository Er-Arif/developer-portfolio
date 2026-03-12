# MD ARIF ALI Portfolio

Personal portfolio website for **MD ARIF ALI**, built to present software engineering work, selected projects, technical skills, and resume downloads.

## Overview

This project is a multi-page portfolio website with:

- a focused landing page
- a dedicated projects archive page
- downloadable resume PDFs
- a custom social preview image
- a small local Node.js server for static serving

The portfolio is positioned around software engineering, web development, automation, and applied AI/ML work.

## Pages

- `index.html` - main portfolio page
- `projects.html` - full projects archive
- `og-image.html` - social preview layout source
- `og-image-minimal.html` - alternate social preview layout

## Tech Stack

- HTML
- CSS
- JavaScript
- Node.js (`server.js` for local serving)
- Python (`generate_resumes.py` for PDF resume generation)
- ReportLab (used locally for resume PDF generation)

## Main Sections

### Home Page

- Hero introduction
- Featured projects
- Expertise
- Skills
- About
- Contact

### Projects Page

Includes the full project archive, currently covering:

- Social Platform Prototype
- Portfolio Website
- LSTM Stock Forecasting
- Text Extraction and Sentiment Analysis
- Language Model Training with nanoGPT
- Facial Recognition in Video
- ATS Resume Analysis and Interview Prep

## Project Structure

```text
.
|-- assets/
|   |-- arif.PNG
|   |-- resume.pdf
|   |-- resume-software-engineer.pdf
|   `-- resume-freelance.pdf
|-- index.html
|-- projects.html
|-- style.css
|-- script.js
|-- server.js
|-- generate_resumes.py
|-- resume-software-engineer.md
|-- resume-freelance.md
|-- og-image.html
|-- og-image-minimal.html
`-- og-image.png
```

## Local Usage

### Option 1: Open as static files

You can open `index.html` directly in the browser.

### Option 2: Run the local server for preview

Use the included Node.js server:

```powershell
node server.js
```

Then open locally:

```text
http://127.0.0.1:3000
```

## Resume Files

Two resume versions are maintained:

- `resume-software-engineer.md`
- `resume-freelance.md`

PDFs are generated into `assets/`:

- `assets/resume-software-engineer.pdf`
- `assets/resume-freelance.pdf`
- `assets/resume.pdf` (copy of the software-engineer version used by the portfolio button)

To regenerate resume PDFs:

```powershell
python generate_resumes.py
```

## Branding and Assets

- Brand mark: `AΛ`
- Brand name: `Arif Ali`
- Social preview image: `og-image.png`
- Primary downloadable resume: `assets/resume.pdf`

## Author

**MD ARIF ALI**  
Software Engineer  
Email: `dev.arifali@gmail.com`


