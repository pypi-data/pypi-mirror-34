#ifndef batoid_rayVector_h
#define batoid_rayVector_h

#include "ray.h"
#include <cmath>
#include <complex>
#include <vector>
#include <Eigen/Dense>

using Eigen::Vector3d;

namespace batoid {
    struct RayVector {
        RayVector() = default;
        RayVector(const RayVector& _rv) = default;
        RayVector(RayVector&& _rv) = default;
        RayVector& operator=(const RayVector& rv) = default;
        RayVector& operator=(RayVector&& rv) = default;

        RayVector(const std::vector<Ray>& _rays) : rays(_rays) {}
        RayVector(std::vector<Ray>&& _rays) : rays(std::move(_rays)) {}

        RayVector(const std::vector<Ray>& _rays, double _wavelength)
            : rays(_rays), wavelength(_wavelength) {}
        RayVector(std::vector<Ray>&& _rays, double _wavelength)
            : rays(std::move(_rays)), wavelength(_wavelength) {}

        // std::vector forwarding
        typename std::vector<Ray>::const_reference operator[](std::vector<Ray>::size_type i) const
            { return rays[i]; }
        typename std::vector<Ray>::iterator begin() noexcept { return rays.begin(); }
        typename std::vector<Ray>::iterator end() noexcept { return rays.end(); }
        typename std::vector<Ray>::size_type size() const noexcept { return rays.size(); }

        // methods
        std::vector<Vector3d> positionAtTime(double t) const;
        RayVector propagatedToTime(double t) const;
        void propagateInPlace(double t);

        std::vector<double> phase(const Vector3d& r, double t) const;
        std::vector<std::complex<double>> amplitude(const Vector3d& r, double t) const;
        std::complex<double> sumAmplitude(const Vector3d& r, double t) const;
        RayVector trimVignetted() const;
        void trimVignettedInPlace();
        std::string repr() const;

        // data
        std::vector<Ray> rays;
        double wavelength{NAN};  // If not NAN, then all wavelengths are this wavelength
    };

    inline std::ostream& operator<<(std::ostream& os, const RayVector& rv) {
        return os << rv.repr();
    }
}

#endif
