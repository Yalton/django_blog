use wasm_bindgen::prelude::*;
use std::env;
use std::fs;
use std::process::Command;

#[wasm_bindgen]
pub fn a_game() {
    let output = Command::new("./game")
        .output()
        .expect("failed to execute process");

    println!("{:?}", output);
}