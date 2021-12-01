use std::{fs::read_to_string, path::Path};

pub fn p1() {
    let input = Path::new(file!()).parent().unwrap().join("input");
    let contents = read_to_string(input).unwrap();

    let values: Vec<i64> = contents
        .lines()
        .map(|l| l.parse::<i64>().unwrap())
        .collect();

    let mut inc = 0;
    for cidx in 1..values.len() {
        let prev = values[cidx - 1];
        let cur = values[cidx];
        if cur > prev {
            inc += 1;
        }
    }
    println!("{}", inc);
}

pub fn p2() {
    let input = Path::new(file!()).parent().unwrap().join("input");
    let contents = read_to_string(input).unwrap();

    let values: Vec<i64> = contents
        .lines()
        .map(|l| l.parse::<i64>().unwrap())
        .collect();

    let prev = values
        .iter()
        .zip(values.iter().skip(1))
        .zip(values.iter().skip(2));
    let cur = prev.clone().skip(1);

    let mut inc = 0;
    for (((p1, p2), p3), ((c1, c2), c3)) in prev.zip(cur) {
        let psum = p1 + p2 + p3;
        let csum = c1 + c2 + c3;
        if csum > psum {
            inc += 1;
        }
    }
    println!("{}", inc);
}

pub fn p2_alt() {
    let input = Path::new(file!()).parent().unwrap().join("input");
    let contents = read_to_string(input).unwrap();

    let values: Vec<i64> = contents
        .lines()
        .map(|l| l.parse::<i64>().unwrap())
        .collect();

    let mut inc = 0;
    for idx in 4..(values.len() + 1) {
        let psum = &values[(idx - 4)..(idx - 1)].iter().sum::<i64>();
        let csum = &values[(idx - 3)..(idx - 0)].iter().sum::<i64>();
        if csum > psum {
            inc += 1;
        }
    }

    println!("{}", inc);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        p1();
    }

    #[test]
    fn test_p2() {
        p2();
        p2_alt();
    }
}
