extern crate config;

use std::process::Command;
use serde::{Deserialize, Serialize};
use std::fmt;
use std::ops::Not;

use std::collections::HashMap;


#[derive(Serialize, Deserialize, Debug, Clone)]
struct Task {
    description: String,
    id: i64,
    priority: Option<String>,
    project: String,
    status: String,
    urgency: f64,
    uuid: String
}

impl fmt::Display for Task {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "description: {}\n
               id: {}\n
               project: {}\n
               status: {}\n
               urgency: {}\n
               uuid: {}",
               self.description,
               self.id,
               self.project,
               self.status,
               self.urgency,
               self.uuid
              )
    }
}

fn main() {

    let mut settings = config::Config::default();
    settings.merge(config::File::with_name("Settings")).unwrap();
    let settings_parsed = settings.try_into::<HashMap<String, String>>().unwrap();

    let nb_tasks = settings_parsed.get("tasks_to_show").map_or(3, |nb| nb.parse().unwrap());

    let appname = settings_parsed.get("dunst_appname").map_or(String::new(), |app| app.parse().unwrap());

    let exclude_project = settings_parsed.get("exclude_project").map_or(String::new(), |proj| proj.parse().unwrap());

    // Read taskwarrior tasks from CLI
    let output = Command::new("task")
        .arg("export")
        .arg("+READY")
        .output()
        .expect("failed to execute process");

    // Check if there's a filter to apply
    let mut tasks : std::vec::Vec<Task> = if exclude_project.len() > 0 {
        serde_json::from_str::<Vec<Task>>(&String::from_utf8(output.stdout).unwrap())
            .expect("Invalid JSON")
            .into_iter()
            .filter(|task| task.project.contains(&exclude_project).not())
            .collect::<Vec<_>>()
    } else {
        serde_json::from_str::<Vec<Task>>(&String::from_utf8(output.stdout).unwrap())
            .expect("Invalid JSON")
            .into_iter()
            .collect::<Vec<_>>()
    };

    // Sort tasks by urgency
    tasks.sort_by(|a, b| b.urgency.partial_cmp(&a.urgency).unwrap());

}
