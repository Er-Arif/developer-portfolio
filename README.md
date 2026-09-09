# MD ARIF ALI Portfolio

Personal portfolio website for **MD ARIF ALI**, built to present software engineering work, selected projects, technical skills, and resume downloads.

## Overview

This project is a multi-page portfolio website with:

- a focused landing page
- a dedicated projects archive page
- downloadable resume PDFs
- a custom social preview image
- a small local Node.js server for static serving

The portfolio is positioned around full-stack product engineering, secure backend systems, automation, and applied AI.

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

Includes the full public project archive, currently covering:

- AI-First CRM Copilot
- Software Distribution Platform
- OTP Authentication Service
- OnePass Password Manager
- Offline Restaurant POS
- Ride Booking Platform
- Interactive Interior Portfolio
- Developer Portfolio

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

## Resume

The portfolio's download button uses `assets/resume.pdf`, the current application-ready full-stack resume. Older Markdown resume sources and the ReportLab generator are retained only as historical source material and should not overwrite the current PDF without review.

## Branding and Assets

- Brand mark: `AΛ`
- Brand name: `Arif Ali`
- Social preview image: `og-image.png`
- Primary downloadable resume: `assets/resume.pdf`

## Author

**MD ARIF ALI**  
Software Engineer  
Email: `dev.arifali@gmail.com`

## Credentials

The certification section links to verified Coursera credentials and copies of Infosys Springboard course certificates in `assets/certificates/`. AWS Cloud Solutions Architect is labelled as a Coursera Professional Certificate. The résumé download includes selected relevant certificates. Duplicate certificates and participation-only documents are not listed as technical qualifications.
