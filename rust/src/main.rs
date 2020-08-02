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
        create_event(task.to_owned());
    }

}


fn create_event(task: Task) -> std::io::Result<()> {
    let mut calendar = ICalendar::new("2.0", "-//Rootbytes Org//TKRW Calendar Version 1.0//EN");
    //https://crates.io/crates/ics

    //let now = Local::now().format("%Y%m%dT%H%M%SZ");

    let mut event = Event::new(task.uuid, "19960704T120000Z");

    if let Some(scheduled) = task.scheduled {
        let end_scheduled = scheduled.parse::<DateTime<Utc>>();
        end_scheduled.unwrap().format("%Y%m%dT%H%M%SZ").to_string();
        event.push(DtStart::new(scheduled));

    };
        //event.push(DtEnd::new(end_scheduled.unwrap().format("%Y%m%dT%H%M%SZ").to_string()));

    // if let Some(due) = task.due {
    //     event.push(DtStart::new(due));
    // }

    return Ok(());


}
