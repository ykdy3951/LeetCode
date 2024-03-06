impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        const ONES : [&str;10] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        const TENS : [&str;10] = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        const HUNS : [&str;10] = ["", "C", "CC", "CCC", "CD" ,"D", "DC", "DCC", "DCCC", "CM"];
        const THOS : [&str;4] = ["", "M", "MM", "MMM"];

        format!("{}{}{}{}", THOS[(num / 1000 % 10) as usize],
                            HUNS[(num / 100 % 10) as usize],
                            TENS[(num / 10 % 10) as usize],
                            ONES[(num % 10) as usize]
        )
    }
}