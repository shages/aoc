
use std::env;
use std::fs::File;
use std::io::prelude::*;

fn main () {
    let args: Vec<String> = env::args().collect();
    let mut file_handle = File::open(&args[1])
                          .expect("file not found");
    let mut contents = String::new();
    file_handle.read_to_string(&mut contents)
               .expect("something went wrong reading the file");

    let chars: Vec<u32> = contents
        .trim()
        .chars()
        .filter_map(|c| c.to_digit(10))
        .collect();

    let mut prev = &chars[chars.len() - 1];
    let mut rep_sum = 0;
    for value in chars.iter() {
        if *prev == *value {
            rep_sum += *value;
        }
        prev = value;
    }
    println!("sum={}", rep_sum);
}
