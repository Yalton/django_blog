use wasm_bindgen::prelude::*;

use std::io;
#[wasm_bindgen]
pub fn main() {
    println!("Hello, world!");
    println!("Please Enter Something");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Something Went Wrong while reading input");
    println!("\nYour input was: {}", input);
}