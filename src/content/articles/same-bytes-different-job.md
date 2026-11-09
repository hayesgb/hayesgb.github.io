---
title: Same Bytes, Different Job; What Makes Telemetry OT In The Age of IoT
pubDate: 2026-11-07
draft: false
---

## One reading, two jobs
A soil moisture probe buried in an orchard row reports 23% volumetric water content, timestamped, every ten minutes. That reading goes two places.
The first is the irrigation controller at the edge of the field, which compares it to a threshold and decides whether to open the valve on zone 4. The second is a cloud platform, where it lands in a table next to a few hundred thousand of its siblings and gets charted for agronomy analytics.
Same bytes. Same timestamp. Same units. One of those destinations is operational technology and the other is information technology, and if your definition of OT can't tell you which, your definition is broken.
Most definitions can't. This post is about why, and about a test that can.

## The standards define a place, not a thing
Ask an industrial engineer what OT is and you will get a diagram: the Purdue model, five or six stacked levels from the physical process at the bottom to the enterprise at the top. OT, by convention, is Levels 0 through 3. IT is Level 4 and up. Level 3.5 is the firewall between them.
That convention is useful and it is also a trick of geography. Theodore Williams' 1989 reference model never used the word OT; it described how a factory's computing was layered. Security practitioners later drew a line across it and called everything below the line OT. Membership is by address, not by nature.
ISA-95 inherits the same levels and gets more specific about one seam, the boundary between Level 3 and Level 4. It defines the objects that cross that boundary: schedules going down, performance reports coming up. But it deliberately stops there. Levels 0 through 2 are "control" and left to someone else, which means the real-time signals that actually touch the equipment are exactly the data the standard chose not to model.
So the two most-cited frameworks agree on where OT sits and say nothing about what makes a piece of data OT. That gap is invisible in a plant, where the controller is physically below the firewall and the data moves up one level at a time.
It is very visible in an irrigation valve that takes its schedule from a cloud platform. The valve controller is Level 1. The platform is somewhere above Level 5. There is nothing in between. The industry has noticed, and the proposed fixes, a new "Level 6" for the cloud, cloud as an extension of Level 5, Zero Trust micro-segmentation, all keep asking where the data sits. None of them asks what the data does.
This post is not about security. The security framing of IT versus OT is a network-architecture problem with its own literature, and I am setting it aside. The question here is about the data itself.

## The obvious proxy fails
If location won't do, the next candidate is shape. OT data, the story goes, is high-frequency, time-series, machine-generated, and tied to physical equipment. IT data is transactional, human-generated, and shaped like a business record.
Every data center on earth refutes this. Servers emit CPU temperatures, fan speeds, and power draw at sub-second intervals. The entire OpenTelemetry ecosystem exists to collect continuous, time-series, machine-generated metrics from physical hardware. Nobody calls any of it OT.
The reverse fails too. A relay protection setting in a substation is a handful of static numbers, changed perhaps once a decade, with no real-time character at all. It is as OT as anything gets, because a wrong value trips a breaker or fails to.
Shape is a correlation, not a definition. Most OT data is time-series because most physical processes are continuous. But the time-series-ness is a symptom of what the data is for, not the thing itself.

## A test that works: is it on the actuation path?
Here is the definition I have landed on.
Data is OT when a system enforces it on an actuation path. It can play one of three roles there:
1. The thing commanded. A setpoint, an export limit, a mode change. The output of a controller headed for an actuator.
2. The thing measured. A reading the controller compares against its target to decide what to do next. The feedback signal.
3. A precondition for a command. A parameter, limit, or state the controller checks before it acts: a ramp rate, a protection setting, a firmware version that gates whether a setpoint is accepted at all.
Everything else is IT. Not lesser, just different: data whose chain of custody ends in a human reading a chart, a model producing a forecast, a report landing in an inbox. Data that terminates in information.
The acronyms were telling us this all along. Information technology produces information. Operational technology produces operations. The question to ask of any piece of telemetry is which one it terminates in.
Control engineers will recognize this as the closed loop. The measured variable, the manipulated variable, and the controller's parameters are the three things that make a feedback loop a loop. Data is OT when it is inside one. Telemetry is OT when it is fed back and IT when it is only logged. The same reading can be both, at different points in its life, which is why the hook at the top of this post is not a paradox.
That also means OT is not a property of a data type or a source system. It is a property of a role, and roles are assigned by the architecture that consumes the data, not the device that produces it.

## Stress-testing the definition
A definition is only as good as the cases that try to break it. Four have been useful.
The relay setting. Static, rarely changed, no real-time character. A time-based or shape-based definition has to call it IT, which is absurd. The actuation-path test handles it cleanly: it is a precondition for a command. Control theory makes the same distinction between signals that flow through a loop and parameters that shape it. Both are inside the loop. Both are OT.
The cloud controller. An irrigation platform pulls tomorrow's weather forecast, computes a watering schedule, and sends a run time to a valve controller in the field. Where does OT begin? Not at a firewall; there isn't one in the right place. It begins at the moment the platform's output becomes a command the controller will enforce. The forecast that produced the schedule is IT. The schedule, once committed, is OT. The platform straddles the line, and that is fine, because the line is drawn through the data, not through the system.
The acknowledgment. When a device receives a command, it typically reports back: received, started, completed. This looks like telemetry; it flows upstream and describes device state. But the server's event logic depends on it. If the acknowledgment doesn't arrive, the server retries, escalates, or falls back. That status message is on the actuation path because the loop does not close without it. Monitoring data by appearance, OT by role.
The pool. A pH probe reads 7.8, a controller compares it to a target of 7.4, an acid pump runs for a few seconds. Textbook loop; the test sorts it instantly. The reading is measured, the pump time is commanded, the target and the maximum daily dose are preconditions, and the same readings logged to a phone app for a weekly trend are IT. But two details earn their place here. The probe's calibration offset is a precondition that drifts on its own, so the loop can dose confidently against a false reading; the calibration state is OT even though nobody would call it telemetry. And many pools have no pump at all. The owner looks at the app, sees 7.8, and pours in a cup of acid. The chart is now on the actuation path, because a person closes the loop by reading it. The line is about the loop, not about whether the actuator is a motor or a human. Data becomes OT the moment someone, or something, commits to act on it.
Each of these cases breaks a location-based or shape-based definition. None of them breaks the role-based one.

## Why this matters for anyone building the pipes
If OT-ness is a role rather than a type, then a float is just a float until something tells you what it is for. That information is not in the schema. A column called soil_moisture_pct looks identical whether it opens a valve or fills a dashboard.
The role lives at the semantic layer: the model that says this reading is a measurement, of this quantity, at this point, consumed by this controller. The Unified Namespace and contextualization movement in industrial data is building exactly that layer, though mostly to make OT data legible to IT consumers. The same metadata, read the other way, tells you which of your telemetry is still OT after it leaves the device.
For a data platform this is not academic. The IT side of the line can tolerate eventual consistency, schema drift, a reprocessing job that runs overnight. The OT side cannot, because a stale or malformed value does not produce a wrong chart; it produces a wrong action. Knowing which of your streams is which is the difference between a data-quality incident and an operational one.
It also tells you where new kinds of consumers belong. A forecasting model that reads telemetry and writes a recommendation is doing IT work on OT inputs. The moment its output is committed as a command the device will enforce, it has crossed the line, and everything downstream has to be held to a different standard: deterministic, bounded, auditable. That boundary is where the interesting questions about AI in physical systems live, and it is the subject of the next post.
For now, the test is simple enough to carry around. Follow the reading. If its chain ends in information, it is IT. If it ends in an operation, it is OT. Same bytes, different job.