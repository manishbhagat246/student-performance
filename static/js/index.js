const words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const colors = ["lightcoral", "lightblue", "lightgreen", "lightsalmon", "lightsteelblue"];

const h1Element = document.querySelector("#textf");
// let interval = null;
// document.querySelector("#textf").onmouseover = Event => {
//     let i = 0;
//     clearInterval(interval);

//     const interval = setInterval(() => {
//         Event.target.innerText = Event.target.innerText.split("")
//             .map((word, index) => {
//                 if (index < i * 2) {
//                     return Event.target.dataset.value[index];
//                 }
//                 return words[Math.floor(Math.random() * 26)]
//             }).join("");
//         if (i >= 6) {
//             clearInterval(interval);
//             h1Element.style.left = "50%";
//             h1Element.style.top = "50%";
//         }
//         i += 1 / 5;
//         const randomColor = colors[Math.floor(Math.random() * colors.length)];
//         h1Element.style.color = randomColor;
//     }, 50);
// }
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

document.querySelector("#textf").onmouseover = event => {  
  let iteration = 0;
  
  clearInterval(interval);
  
  interval = setInterval(() => {
    event.target.innerText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if(index < iteration) {
          return event.target.dataset.value[index];
        }
      
        return letters[Math.floor(Math.random() * 26)]
      })
      .join("");
    
    if(iteration >= event.target.dataset.value.length){ 
      clearInterval(interval);
    }
    // const randomColor = colors[Math.floor(Math.random() * colors.length)];
    // h1Element.style.color = randomColor;
    iteration += 1 / 2;
  }, 30);
}
