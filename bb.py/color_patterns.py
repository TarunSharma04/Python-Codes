from bs4 import BeautifulSoup

# Replace `inspect_code` with the actual inspect code you provided
inspect_code = """
<div class="kline">
    <div class="title">
        <div class="red">
            Red:92
        </div>
        <div class="green">
            Green:109
        </div>
        <div class="violet">
            Violet:16
        </div>
    </div>
    <div class="switchBox">
        <button class="van-button van-button--small van-button--default">
            <span class="van-button__text">ShowPeriod</span>
        </button>
        <button class="van-button van-button--small van-button--primary">
            <span class="van-button__text">ShowOpenNum</span>
        </button>
    </div>
    <div class="box">
        <div class="grid">
            <div class="row">
                <div class="index">
                    ...
                </div>
                ...
            </div>
            ...
        </div>
    </div>
</div>
"""

# Parse the inspect code using BeautifulSoup
soup = BeautifulSoup(inspect_code, "html.parser")

# Find the <div> elements with color patterns under the <div class="title"> element
color_elements = soup.find("div", class_="title").find_all("div", class_=["red", "green", "violet"])

# Extract the color patterns from the HTML elements
color_patterns = []
for element in color_elements:
    # Extract the color pattern from the element's text content
    color_pattern = element.get_text().strip().split(":")[0].strip()
    color_patterns.append(color_pattern)

# Print the extracted color patterns
print("Extracted Color Patterns:")
for pattern in color_patterns:
    print(pattern)
