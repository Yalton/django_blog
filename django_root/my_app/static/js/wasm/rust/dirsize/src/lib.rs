use wasm_bindgen::prelude::*;
use std::env;
use std::fs;

#[wasm_bindgen]
pub fn fileread() {
    let filename = "/usr/src/app/staticfiles/filesize"
    // --snip--
    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    println!("Size:\n{}", contents);
}