import os

def create_resume_pdf(filename="assets/Sumit_Rai_Resume.pdf"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    width = 595.28
    height = 841.89
    stream_lines = []
    
    def rgb(r, g, b):
        return f"{r/255.0:.3f} {g/255.0:.3f} {b/255.0:.3f}"
    
    c_dark = rgb(22, 20, 18)
    c_orange = rgb(224, 99, 30)
    c_gray = rgb(90, 85, 80)
    c_light_gray = rgb(220, 216, 210)
    c_bg = rgb(253, 251, 247)
    
    # Background
    stream_lines.append(f"{c_bg} rg 0 0 {width:.2f} {height:.2f} re f")
    
    # Accent top border
    stream_lines.append(f"{c_orange} rg 36 {height - 24:.2f} {width - 72:.2f} 4 re f")
    
    def esc(text):
        # Replace non-ascii characters with clean ascii equivalents
        text = text.replace('—', '-').replace('–', '-').replace('·', '|').replace('•', '-')
        return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    
    y = height - 58
    
    # Name
    stream_lines.append("BT")
    stream_lines.append("/F2 24 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('Sumit Rai')}) Tj")
    stream_lines.append("ET")
    
    # Title
    y -= 20
    stream_lines.append("BT")
    stream_lines.append("/F2 10.5 Tf")
    stream_lines.append(f"{c_orange} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('SENIOR PRODUCT DESIGNER  |  AI BUILDER')}) Tj")
    stream_lines.append("ET")
    
    # Contact
    y -= 15
    contact_text = "Delhi, India   |   sumitraiworks@gmail.com   |   linkedin.com/in/isumitrai   |   isumitrai.github.io"
    stream_lines.append("BT")
    stream_lines.append("/F1 8.5 Tf")
    stream_lines.append(f"{c_gray} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc(contact_text)}) Tj")
    stream_lines.append("ET")
    
    # Divider
    y -= 12
    stream_lines.append(f"{c_light_gray} RG 0.8 w 40 {y:.2f} m {width - 40:.2f} {y:.2f} l S")
    
    # Section: Summary
    y -= 18
    stream_lines.append("BT")
    stream_lines.append("/F2 10 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('PROFESSIONAL SUMMARY')}) Tj")
    stream_lines.append("ET")
    
    summary_lines = [
        "Product Designer with 7+ years of product design experience since 2019 and 10+ years of overall design experience.",
        "Experienced in designing digital products across SaaS, AI, EdTech, FinTech, HealthTech, and consumer platforms.",
        "Focused on product strategy, user experience, interaction design, visual design, and building thoughtful digital experiences."
    ]
    y -= 14
    for line in summary_lines:
        stream_lines.append("BT")
        stream_lines.append("/F1 8.5 Tf")
        stream_lines.append(f"{c_gray} rg")
        stream_lines.append(f"40 {y:.2f} Td")
        stream_lines.append(f"({esc(line)}) Tj")
        stream_lines.append("ET")
        y -= 12
        
    y -= 3
    stream_lines.append(f"{c_light_gray} RG 0.8 w 40 {y:.2f} m {width - 40:.2f} {y:.2f} l S")
    
    # Section: Experience
    y -= 18
    stream_lines.append("BT")
    stream_lines.append("/F2 10 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('PROFESSIONAL EXPERIENCE')}) Tj")
    stream_lines.append("ET")
    
    experiences = [
        {
            "role": "Founding Designer",
            "company": "Raimage Design",
            "period": "2025 - Present",
            "location": "New Delhi, India",
            "bullets": [
                "Directing product design, brand identity systems, and AI-native interface explorations for high-growth ventures.",
                "Spearheading product strategy, component libraries, and rapid interactive prototyping combining Figma and code.",
                "Partnering closely with founders and engineering leaders to translate complex workflows into intuitive user experiences."
            ]
        },
        {
            "role": "Senior Product Designer",
            "company": "Edfora Infotech",
            "period": "2023 - 2025",
            "location": "New Delhi, India",
            "bullets": [
                "Led end-to-end product design across web and mobile platforms for FIITJEE educational products and learning platforms.",
                "Collaborated with product leadership on research-backed roadmaps, multi-tenant dashboards, and learner portals.",
                "Architected a unified design system that accelerated cross-functional design-to-development velocity by 35%."
            ]
        },
        {
            "role": "Product Designer",
            "company": "Design Matra",
            "period": "2021 - 2023",
            "location": "New Delhi, India",
            "bullets": [
                "Owned user experience design for high-traffic SaaS and mobile products across FinTech, HealthTech, and E-Commerce.",
                "Redesigned core onboarding, search, and checkout flows, driving measurable gains in user conversion and retention.",
                "Conducted generative usability research, rapid iterative prototyping, and comprehensive responsive design audits."
            ]
        },
        {
            "role": "Graphic & Interface Designer",
            "company": "Kitaro Trading",
            "period": "2015 - 2021",
            "location": "New Delhi, India",
            "bullets": [
                "Designed digital brand identities, marketing assets, and responsive web interfaces across diverse consumer product portfolios.",
                "Created foundational brand guidelines, design tokens, and multi-channel creative visual communication assets."
            ]
        }
    ]
    
    for exp in experiences:
        y -= 15
        stream_lines.append("BT")
        stream_lines.append("/F2 9.5 Tf")
        stream_lines.append(f"{c_dark} rg")
        stream_lines.append(f"40 {y:.2f} Td")
        stream_lines.append(f"({esc(exp['role'])}) Tj")
        stream_lines.append("ET")
        
        stream_lines.append("BT")
        stream_lines.append("/F2 8.5 Tf")
        stream_lines.append(f"{c_orange} rg")
        stream_lines.append(f"480 {y:.2f} Td")
        stream_lines.append(f"({esc(exp['period'])}) Tj")
        stream_lines.append("ET")
        
        y -= 11.5
        stream_lines.append("BT")
        stream_lines.append("/F1 8.5 Tf")
        stream_lines.append(f"{c_gray} rg")
        stream_lines.append(f"40 {y:.2f} Td")
        stream_lines.append(f"({esc(exp['company'] + '  |  ' + exp['location'])}) Tj")
        stream_lines.append("ET")
        
        y -= 10.5
        for b in exp["bullets"]:
            stream_lines.append("BT")
            stream_lines.append("/F2 8 Tf")
            stream_lines.append(f"{c_orange} rg")
            stream_lines.append(f"46 {y:.2f} Td")
            stream_lines.append("(-) Tj")
            stream_lines.append("ET")
            
            stream_lines.append("BT")
            stream_lines.append("/F1 8.2 Tf")
            stream_lines.append(f"{c_dark} rg")
            stream_lines.append(f"54 {y:.2f} Td")
            stream_lines.append(f"({esc(b)}) Tj")
            stream_lines.append("ET")
            y -= 10.5
            
    y -= 3
    stream_lines.append(f"{c_light_gray} RG 0.8 w 40 {y:.2f} m {width - 40:.2f} {y:.2f} l S")
    
    # Section: Selected Projects
    y -= 17
    stream_lines.append("BT")
    stream_lines.append("/F2 10 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('SELECTED FEATURED PROJECTS')}) Tj")
    stream_lines.append("ET")
    
    projects_info = [
        ("EduManage", "SaaS Educational Management Dashboard - Unified student, staff & CMS workflows."),
        ("Quayo Basket", "Grocery App & Brand Identity - Streamlined mobile catalog, cart & checkout UX."),
        ("Musafir", "Travel Experience Marketplace - High-converting destination booking experience."),
        ("Community", "Student Learning Hub - Peer learning workflows, engagement channels & resource discovery.")
    ]
    
    y -= 12.5
    for pname, pdesc in projects_info:
        stream_lines.append("BT")
        stream_lines.append("/F2 8.5 Tf")
        stream_lines.append(f"{c_dark} rg")
        stream_lines.append(f"40 {y:.2f} Td")
        stream_lines.append(f"({esc(pname + ': ')}) Tj")
        stream_lines.append("ET")
        
        stream_lines.append("BT")
        stream_lines.append("/F1 8.2 Tf")
        stream_lines.append(f"{c_gray} rg")
        stream_lines.append(f"105 {y:.2f} Td")
        stream_lines.append(f"({esc(pdesc)}) Tj")
        stream_lines.append("ET")
        y -= 10.5
        
    y -= 3
    stream_lines.append(f"{c_light_gray} RG 0.8 w 40 {y:.2f} m {width - 40:.2f} {y:.2f} l S")
    
    # Section: Skills & Tools
    y -= 17
    stream_lines.append("BT")
    stream_lines.append("/F2 10 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('CORE COMPETENCIES & TOOLKIT')}) Tj")
    stream_lines.append("ET")
    
    y -= 13
    stream_lines.append("BT")
    stream_lines.append("/F2 8.5 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('Design & Strategy:')}) Tj")
    stream_lines.append("ET")
    
    stream_lines.append("BT")
    stream_lines.append("/F1 8.2 Tf")
    stream_lines.append(f"{c_gray} rg")
    stream_lines.append(f"135 {y:.2f} Td")
    stream_lines.append(f"({esc('Product Strategy, UX Research, Interaction Design, Design Systems, Information Architecture, Wireframing')}) Tj")
    stream_lines.append("ET")
    
    y -= 11
    stream_lines.append("BT")
    stream_lines.append("/F2 8.5 Tf")
    stream_lines.append(f"{c_dark} rg")
    stream_lines.append(f"40 {y:.2f} Td")
    stream_lines.append(f"({esc('Tools & Technology:')}) Tj")
    stream_lines.append("ET")
    
    stream_lines.append("BT")
    stream_lines.append("/F1 8.2 Tf")
    stream_lines.append(f"{c_gray} rg")
    stream_lines.append(f"135 {y:.2f} Td")
    stream_lines.append(f"({esc('Figma, Framer, Webflow, VS Code, Cursor, HTML/CSS/JS, AI Workflows (Midjourney, LLMs), Adobe Illustrator, Photoshop')}) Tj")
    stream_lines.append("ET")
    
    # Footer
    y -= 18
    stream_lines.append("BT")
    stream_lines.append("/F1 7.5 Tf")
    stream_lines.append(f"{c_gray} rg")
    stream_lines.append(f"175 {y:.2f} Td")
    stream_lines.append(f"({esc('Sumit Rai Portfolio   |   isumitrai.github.io   |   sumitraiworks@gmail.com')}) Tj")
    stream_lines.append("ET")
    
    stream_bytes = "\n".join(stream_lines).encode("latin1")
    stream_len = len(stream_bytes)
    
    objects = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width:.2f} {height:.2f}] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>".encode("latin1"))
    objects.append(f"<< /Length {stream_len} >>\nstream\n".encode("latin1") + stream_bytes + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
    
    pdf = bytearray()
    pdf.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    
    offsets = [0]
    for i, obj in enumerate(objects):
        offsets.append(len(pdf))
        pdf.extend(f"{i+1} 0 obj\n".encode("latin1"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")
        
    xref_offset = len(pdf)
    num_objects = len(objects) + 1
    pdf.extend(f"xref\n0 {num_objects}\n".encode("latin1"))
    pdf.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("latin1"))
        
    pdf.extend(f"trailer\n<< /Size {num_objects} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("latin1"))
    
    with open(filename, "wb") as f:
        f.write(pdf)
        
    print(f"Generated {filename} successfully! Size: {len(pdf)} bytes")

if __name__ == "__main__":
    create_resume_pdf()
