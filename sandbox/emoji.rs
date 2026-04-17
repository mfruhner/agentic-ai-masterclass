fn main() {
    let animal_data = [
        ("🐶 Dog", "🤚", "Woof!"),
        ("🐱 Cat", "👋", "Meow!"),
        ("🐦 Bird", "🤏", "Tweet!"),
        ("🐭 Mouse", "✌️", "Squeak!"),
        ("🐮 Cow", "🤞", "Moo!"),
        ("🐸 Frog", "👊", "Croak!"),
        ("🐘 Elephant", "👌", "Toot!"),
        ("🦊 Fox", "🤟", "Ring-ding-ding!"),
    ];

    for (animal, hand, sound) in animal_data {
        println!("{} {} — {}", animal, hand, sound);
    }
}
