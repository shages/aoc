
use std::env;
use std::fs::File;
use std::io::prelude::*;

struct Config {
    query: String,
    filename: String,
}

impl Config {
    fn new(args: &[String]) -> Self {
        Config {
            query: args[1].clone(),
            filename: args[2].clone()
        }
    }
}

fn main () {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args);

    let mut file_handle = File::open(config.filename).expect("file not found");
    let mut contents = String::new();
    file_handle.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
    println!("With text:\n{}", contents);

    let contents: Vec<u32> = contents
        .trim()
        .chars()
        .filter_map(|c| c.to_digit(10))
        .collect();
    println!("contents now={:?}", contents);

    // add up all repetitions
    let mut rep_sum = 0;
    let mut prev = contents.last().clone();
    let mut pvalue = 10000000;
    match prev {
        None => return,
        Some(v) => {
            pvalue = *v;
        }
    }
    for value in contents.iter() {
        println!("value={}", value);
        if pvalue == *value {
            println!("repetition!");
            rep_sum += value;
        }
        pvalue = *value;
    }
    println!("rep_sum={}", rep_sum);
}
