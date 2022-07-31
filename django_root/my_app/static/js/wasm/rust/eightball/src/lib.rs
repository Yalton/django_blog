extern crate getrandom;
use wasm_bindgen::prelude::*;
use getrandom;

#[wasm_bindgen]
pub fn eightball(a: String){
    let answers = ["It is certain","It is decidedly so.","Without a doubt.","Yes: definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Very doubtful.","Outlook not so good.","My sources say no.","My reply is no.","Don’t count on it.","Concentrate and ask again.","Cannot predict now.","Better not tell you now.","Ask again later.","Reply hazy, try again."];
    
    let randnum = getrandom::thread_rng().gen_range(0, answers.len() - 1);

    println!("\nThe question was: {}\n The 8 ball says: {}", a, answers[randnum])
}