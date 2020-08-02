extern crate config;
use std::process::Command;
extern crate ics;
use std::io::Result;

use ics::properties::{Categories, Description, DtEnd, DtStart, Organizer, Status, Summary};
use ics::{escape_text, Event, ICalendar};

// Project sources
pub use self::structs::Task;
mod structs;


fn main() {

    // Read taskwarrior tasks from CLI
    let output = Command::new("task")
        .arg("export")
        .arg("+READY")
        .output()
        .expect("failed to execute process");

    // Check if there's a filter to apply
    let mut tasks : std::vec::Vec<Task> = serde_json::from_str::<Vec<Task>>(&String::from_utf8(output.stdout).unwrap())
        .expect("Invalid JSON")
        .into_iter()
        .collect::<Vec<_>>();

    // Sort tasks by urgency
    tasks.sort_by(|a, b| b.urgency.partial_cmp(&a.urgency).unwrap());


    for task in &tasks {
        println!("{:?}", task);
    }
}


fn create_event(task: Task) -> std::io::Result<()> {

    let mut calendar = ICalendar::new("2.0", "-//Rootbytes Org//TKRW Calendar Version 1.0//EN");
    //https://crates.io/crates/ics
    //let mut event = Event::new(


}
