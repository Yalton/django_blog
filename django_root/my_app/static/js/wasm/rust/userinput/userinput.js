// Import our outputted wasm ES6 module
// Which, export default's, an initialization function
import init from "./pkg/userinput.js";

const runWasm = async() => {

    const userinput = await init("./pkg/userinput_bg.wasm");

    const inputout = userinput.main();


    // document.body.textContent = `${inputout}`;
};
runWasm();