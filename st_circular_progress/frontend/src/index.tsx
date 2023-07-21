import { Streamlit, RenderData } from "streamlit-component-lib"

// Add text and a button to the DOM. (You could also add these directly
// to index.html.)
var head = document.getElementsByTagName('HEAD')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = 'st_circular_progress/frontend/public/progress.css';
head.appendChild(link);
const container = document.body.appendChild(document.createElement("div"))
container.className = "progress-bar-container"
const header = container.appendChild(document.createElement("div"))
header.className = "header-label"
const header_text = header.appendChild(document.createTextNode(""))
const progress_bar = container.appendChild(document.createElement("div"))
progress_bar.className = "progress-bar html"
progress_bar.appendChild(document.createElement("progress"))
progress_bar.id = "html"
progress_bar.setAttribute("min", "0")
progress_bar.setAttribute("max", "100")


function onRender(event: Event): void {
  const data = (event as CustomEvent<RenderData>).detail
  let label = data.args["label"]
  let progress_value = data.args["value"]
  let size = data.args["size"]
  let track_color = data.args["track_color"]
  let color = data.args["color"]

  document.documentElement.style
    .setProperty('--bar-track-color', track_color)
  getComputedStyle(document.documentElement).getPropertyValue('--bar-track-color')
  document.documentElement.style
    .setProperty('--bar-progress-color', color)
  getComputedStyle(document.documentElement).getPropertyValue(' --bar-progress-color')

  if (size === `small`) {
    document.documentElement.style
      .setProperty('--size-px', `50px`)
    getComputedStyle(document.documentElement).getPropertyValue('--size-px')
    Streamlit.setFrameHeight(150)
  }
  if (size === `medium`) {
    document.documentElement.style
      .setProperty('--size-px', `100px`)
    getComputedStyle(document.documentElement).getPropertyValue('--size-px')
    Streamlit.setFrameHeight(250)
  }

  if (size === `large`) {
    document.documentElement.style
      .setProperty('--size-px', `150px`)
    getComputedStyle(document.documentElement).getPropertyValue('--size-px')
    Streamlit.setFrameHeight(300)
  }

  header_text.textContent = `${label}` + String.fromCharCode(160)
  document.documentElement.style
    .setProperty('--progres-bar-value', progress_value)
  getComputedStyle(document.documentElement).getPropertyValue('--progres-bar-value')
  let speed = (progress_value / 100)
  document.documentElement.style
    .setProperty('--animation-lenght', `${speed}s`)
  getComputedStyle(document.documentElement).getPropertyValue('--animation-lenght')

  Streamlit.setComponentValue(progress_value.text)

}
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
