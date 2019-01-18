## Cosmograph
A python library for storage and retrieval of arbitrary mapping and historical data; this data is served as a Cosmograph, an object that can render annotated maps

a basic heirarchy:

1. A **Multiverse** has...
2. one or more **Universes**
3. which has features, including 
  - **Stars**
  - **Planets**
4. Which have associated **Living Maps**
  - Living maps are maps whose contents are dependent on time; most locations change over time, and maps should represent this
5. Containing **Annotations** tied to place(s) and time(s)
  - annotations are tied to:
    - a point in or interval of time
    - location(s)
    - objects
    - information sources and their information
      - e.g., a person saying something in a place

A cosmograph requires:
- A **Cosmograph module** (**CGM**) to instantiate base cosmograph
  - a fictional or non-fictional universe
