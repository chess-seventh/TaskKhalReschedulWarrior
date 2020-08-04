extern crate config;
extern crate ics;
extern crate chrono;

use std::process::Command;
use std::io::Result;
use ics::properties::{Categories, Description, DtEnd, DtStart, Organizer, Status, Summary};
use ics::{escape_text, Event, ICalendar};
use chrono::Local;
use chrono::prelude::*;


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
        match create_event(task.to_owned()) {
            Ok(_) => println!("All good mate!"),
            Err(_) => println!("It failed mate!")
        }
    }

}


fn create_event(task: Task) -> std::io::Result<()> {
    println!("\n\n====================");
    println!("We're in the create_event function !");
    println!("====================\n");

    let calendar = ICalendar::new("2.0", "-//Rootbytes Org//TKRW Calendar Version 1.0//EN");
    //https://crates.io/crates/ics

    //let now = Local::now().format("%Y%m%dT%H%M%SZ");

    let mut event = Event::new(task.uuid, "19960704T120000Z");

    if let Some(scheduled) = task.scheduled {
        let end_scheduled = match scheduled.parse::<DateTime<Utc>>() {
            Ok(e) => scheduled.format("%Y%m%dT%H%M%SZ").to_string(),
        };
        //end_scheduled.unwrap_err();
        //match end_scheduled.unwrap().format("%Y%m%dT%H%M%SZ").to_string() {

        //}
        //println!("this is the values of end_scheduled >>>>         {:?}", end_scheduled);
        event.push(DtStart::new(scheduled));
    };

    // if let Some(due) = task.due {
    //     event.push(DtStart::new(due));
    // }

    return Ok(());


}
