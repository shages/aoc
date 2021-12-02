use std::{fs::read_to_string, path::Path, str::FromStr};

fn read_input() -> String {
    let input = Path::new(file!()).parent().unwrap().join("input");
    read_to_string(input).unwrap()
}

fn parse_lines() -> Vec<String> {
    read_input().lines().map(String::from).collect()
}

fn parse_lines_int() -> Vec<i64> {
    parse_lines()
        .iter()
        .map(|line| line.parse::<i64>().unwrap())
        .collect()
}

fn parse_lines_float() -> Vec<f64> {
    parse_lines()
        .iter()
        .map(|line| line.parse::<f64>().unwrap())
        .collect()
}

fn parse_lines_vals<T>() -> Vec<T>
where
    T: FromStr,
    <T as FromStr>::Err: std::fmt::Debug,
{
    parse_lines()
        .iter()
        .map(|line| line.parse::<T>().unwrap())
        .collect()
}

pub fn p1() -> i64 {
    let mut h = 0;
    let mut d = 0;
    for shit in parse_lines() {
        match shit.split_whitespace().collect::<Vec<&str>>().as_slice() {
            ["forward", v] => h += v.parse::<i64>().unwrap(),
            ["up", v] => d -= v.parse::<i64>().unwrap(),
            ["down", v] => d += v.parse::<i64>().unwrap(),
            _ => {}
        }
    }
    h * d
}

pub fn p2() -> i64 {
    let mut h = 0;
    let mut d = 0;
    let mut a = 0;
    for shit in parse_lines() {
        match shit.split_whitespace().collect::<Vec<&str>>().as_slice() {
            ["forward", v] => {
                h += v.parse::<i64>().unwrap();
                d += v.parse::<i64>().unwrap() * a;
            }
            ["up", v] => a -= v.parse::<i64>().unwrap(),
            ["down", v] => a += v.parse::<i64>().unwrap(),
            _ => {}
        }
    }
    h * d
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        assert_eq!(p1(), 1840243);
    }

    #[test]
    fn test_p2() {
        assert_eq!(p2(), 1727785422);
    }
}
