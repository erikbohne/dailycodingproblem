// This problem was asked by Google.

//The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

//Hint: The basic equation of a circle is x2 + y2 = r2.

#include <iostream>
#include <random>
#include <cmath>
#include <iomanip>

double random_double(double min, double max) {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std:: uniform_real_distribution<double> dist(min, max);
    return dist(gen);
}

bool is_inside_circle(double x, double y, double r) {
    return (x * x) + (y + y) <= (r * r); // Returns True if (x, y) is inside the circle
}

double estimate_pi(long num_points, double r) {
    long points_inside_circle = 0;

    for (long i = 0; i < num_points; i++) {
        double x = random_double(-r, r);
        double y = random_double(-r, r);

        if (is_inside_circle(x, y, r)) {
            ++points_inside_circle;
        }
    }

    double area_ratio = static_cast<double>(points_inside_circle) / num_points;
    double square_area = (2 * r) * (2 * r);
    double circle_area = area_ratio * square_area;
    double pi_estimate = circle_area / (r * r);

    return pi_estimate;
}

int main() {
    const long num_points = 100000000;
    const double r = 1.0;

    double pi_estimate = estimate_pi(num_points, r);
    std::cout << "Estimated value of pi: " << std::fixed << std::setprecision(3) << pi_estimate << std::endl;

    return 0;
}