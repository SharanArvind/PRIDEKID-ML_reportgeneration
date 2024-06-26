import pickle
from pride_model import PRIDEModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the model from the pickle file
with open('pride_model.pkl', 'rb') as f:
    pride_model = pickle.load(f)

def generate_report_pdf(name, accuracy, speed, consistency, output_filename):
    report = pride_model.generate_report(name, accuracy, speed, consistency)

    # Create PDF
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "PRIDE Model Report")
    c.line(100, 745, 500, 745)  # underline the title

    # Write input details
    c.setFont("Helvetica", 12)
    c.drawString(100, 710, f"Name: {name}")
    c.drawString(100, 690, f"Accuracy: {accuracy}%")
    c.drawString(100, 670, f"Speed: {speed}%")
    c.drawString(100, 650, f"Consistency: {consistency}%")

    # Write report content
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 620, "Report:")
    c.setFont("Helvetica", 12)
    lines = report.split("\n")
    y_position = 600
    for line in lines:
        if y_position < 80:
            c.showPage()
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, 750, "PRIDE Model Report (Continued)")
            c.line(100, 745, 500, 745)
            c.setFont("Helvetica", 12)
            y_position = 700
        c.drawString(100, y_position, line.strip())
        y_position -= 20

    c.save()
    print(f"Report saved as {output_filename}")

def get_inputs():
    name = input("Enter the name: ")
    accuracy = float(input("Enter the accuracy percentage: "))
    speed = float(input("Enter the speed percentage: "))
    consistency = float(input("Enter the consistency percentage: "))
    return name, accuracy, speed, consistency

def main():
    name, accuracy, speed, consistency = get_inputs()
    output_filename = input("Enter the output filename (e.g., report.pdf): ")
    generate_report_pdf(name, accuracy, speed, consistency, output_filename)

if __name__ == "__main__":
    main()
