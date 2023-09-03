# Geometric-Nonlinear-Controller-for-High-Performance-Quadrotor-Flight
This repository presents a nonlinear controller for quadrotors, optimized for the CrazyFlie 2.0. Harnessing geometric mechanics, it supports aggressive flights, sharp turns, and inverted loops. The design blends vector math with computational modeling, elevating UAV agility and stability.

## Overview

### Geometric Nonlinear Controller for Quadrotors

This project is centered around the implementation and testing of a Geometric Nonlinear Controller for quadrotors, enabling aggressive maneuvers such as high-speed flights, sharp turns, and even inverted loops. The primary platform used is the CrazyFlie 2.0 by Bitcraze, emphasizing the design and simulation of control algorithms that assure stability and high-flight performance.

## Table of Contents
- [Controller Description](#controller-description)
- [System Details](#system-details)
- [Project Workflow](#project-workflow)
- [Conclusion](#conclusion)

## Controller Description

### Design Basis
- The design approach builds upon geometric intuition, leveraging the quadrotor's b3 axis to tilt and orient in the desired direction.
- The controller draws inspiration from the work in [1] and streamlines the controller detailed in [2].

### Algorithm Layout
- The controller architecture bifurcates into two significant components: an attitude controller and a position controller.
- The algorithm leans towards compact vector forms over the traditional backstepping assumption.

### Implementation Steps
1. Compute the total commanded force `Fdes` that factors in gravitational forces.
2. Ascertain input `u1` by projecting `Fdes` onto the quadrotor's b3 axis.
3. Determine the desired rotation matrix `Rdes` by ensuring proper alignment of the quadrotor's bi axis.
4. Gauge the orientation error vector `eR` to evaluate the variance between the desired and actual orientations.
5. Finally, deduce the control input `u2` by employing torque values that reduce the orientation error.

## System Details

### Quadrotor Platform: CrazyFlie 2.0
- **Motor-to-motor distance:** 92 mm
- **Mass:** 30 g (including the battery)
- **Feedback Mechanism:** Onboard IMU that provides feedback on angular velocities and accelerations.

### Software Integration
- High-level commands and position controls are orchestrated in Python and transmitted to the robot via CrazyRadio (2.4GHz).
- The project focuses on testing the attitude control in simulations, though it's executed onboard.

### Key Physical Parameters
- **Mass (m):** 0.030 kg
- **Motor axis distance from the center of mass (l):** 0.046m
- **Inertia matrix ([IC]bi):** Diagonal with predetermined values

## Project Workflow

### Code Framework
- This project utilizes a packet encompassing code stubs, with the core simulator embedded in the `flightsim` directory.
- Implementation zeroes in on `code/sandbox.py`, which, when launched, simulates quadrotor flight based on the controller logic.

### Key Deliverables
- **Waypoint Trajectory Generator (`waypoint traj.py`):** Designed to retain a set of aspired waypoints for the quadrotor, dictating a state for each time juncture.
- **SE3 Controller (`se3 control.py`):** This is the linchpin that drives the quadrotor towards a state as outlined by the trajectory generator. It gives out motor speed commands contingent on the quadrotor's state and the aspired state.

## Conclusion
The project highlights the capabilities and benefits of a geometric nonlinear controller for quadrotors. The execution hinged on mathematical models, geometric insights, and simulated platforms to exhibit the stability and efficiency of the controller.



