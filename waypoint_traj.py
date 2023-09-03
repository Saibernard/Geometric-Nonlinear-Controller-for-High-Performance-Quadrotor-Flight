import numpy as np


class WaypointTraj(object):

    """


    """

    def __init__(self, points):

        """

        This is the constructor for the Trajectory object. A fresh trajectory

        object will be constructed before each mission. For a waypoint

        trajectory, the input argument is an array of 3D destination

        coordinates. You are free to choose the times of arrival and the path

        taken between the points in any way you like.


        You should initialize parameters and pre-compute values such as

        polynomial coefficients here.


        Inputs:

            points, (N, 3) array of N waypoint coordinates in 3D

        """


        # STUDENT CODE HERE

        self.waypoints = points

        self.directions = np.zeros((self.waypoints.shape[0] -1, self.waypoints.shape[1]))

        self.segment_distances = np.zeros((self.directions.shape[0], 1))

        self.desired_velocities = np.zeros((self.directions.shape[0], self.waypoints.shape[1]))

        self.start_times = np.zeros((self.directions.shape[0], 1))


        self.velocity = 2.26

        time_elapsed = 0

        for i in range(len(self.waypoints) - 1):

            point_diff = self.waypoints[i + 1] - self.waypoints[i]

            distance = np.linalg.norm(point_diff)

            self.segment_distances[i] = distance

            self.directions[i] = point_diff / distance

            self.desired_velocities[i] = self.velocity * self.directions[i]

            time_elapsed += distance / self.velocity

            self.start_times[i] = time_elapsed


        self.desired_velocities = np.vstack([self.desired_velocities, np.zeros((1, 3))])

        self.directions = np.vstack([self.directions, np.zeros((1, 3))])

        self.segment_distances = np.vstack([self.segment_distances, np.zeros((1,))])

        self.directions = np.vstack([self.directions, np.zeros((1, 3))])

        self.start_times = np.insert(self.start_times, 0, 0)


    def update(self, t):

        """

        Given the present time, return the desired flat output and derivatives.


        Inputs

            t, time, s

        Outputs

            flat_output, a dict describing the present desired flat outputs with keys

                x,        position, m

                x_dot,    velocity, m/s

                x_ddot,   acceleration, m/s**2

                x_dddot,  jerk, m/s**3

                x_ddddot, snap, m/s**4

                yaw,      yaw angle, rad

                yaw_dot,  yaw rate, rad/s

        """

        x        = np.zeros((3,))

        x_dot    = np.zeros((3,))

        x_ddot   = np.zeros((3,))

        x_dddot  = np.zeros((3,))

        x_ddddot = np.zeros((3,))

        yaw = 0.0

        yaw_dot = 0


        # STUDENT CODE HERE


        if t >= self.start_times[-1]:

            x_dot = np.zeros((3,))

            x = self.waypoints[-1]

        else:

            for i in range(len(self.start_times)):

                if self.start_times[i] <= t < self.start_times[i + 1]:

                    x_dot = self.velocity * self.directions[i]

                    x = self.waypoints[i] + x_dot * (t - self.start_times[i])

                    break


        flat_output = { 'x':x, 'x_dot':x_dot, 'x_ddot':x_ddot, 'x_dddot':x_dddot, 'x_ddddot':x_ddddot,

                        'yaw':yaw, 'yaw_dot':yaw_dot}

        return flat_output


