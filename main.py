import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    # Get the absolute path to your index.html
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = f"file://{os.path.join(current_dir, 'index.html')}"
    pdf_path = os.path.join(current_dir, 'resources', 'resume.pdf')
    
    # Ensure the resources directory exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    print(f"Loading {html_path}...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Load the HTML file
        await page.goto(html_path)
        
        # Emulate the print media type (optional, but good for PDFs)
        await page.emulate_media(media="print")
        
        # Generate the PDF
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"}
        )
        
        await browser.close()
        
    print(f"Success! PDF generated at: {pdf_path}")
    print("Don't forget to update the 'Download CV' link in your index.html to point to 'resources/resume.pdf'")

if __name__ == '__main__':
    asyncio.run(generate_pdf())
