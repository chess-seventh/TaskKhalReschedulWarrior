use serde::{Deserialize, Serialize};
use std::fmt;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Task {
    pub description: String,
    pub id: i64,
    pub priority: Option<String>,
    pub project: String,
    pub status: String,
    pub urgency: f64,
    pub scheduled: Option<String>,
    pub due: Option<String>,
    pub uuid: String
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

