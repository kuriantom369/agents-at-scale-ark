"""Authentication configuration for ark-api routes."""

from typing import Set, Pattern
import re

# Routes that should NOT be authenticated (public endpoints)
# All other routes will be protected by default
PUBLIC_ROUTES: Set[str] = {
    "/health",
    "/ready",
    "/docs",
    "/openapi.json",
    "/redoc"
}

def is_route_authenticated(path: str) -> bool:
    """
    Check if a route path requires authentication.
    By default, all routes are protected except those in PUBLIC_ROUTES.
    
    Args:
        path: The route path to check
        
    Returns:
        True if the route requires authentication, False otherwise
    """
    # Check if it's explicitly public - if so, don't authenticate
    if path in PUBLIC_ROUTES:
        return False
    
    # All other routes are protected by default
    return True

def get_public_routes() -> Set[str]:
    """Get all public routes that don't require authentication."""
    return PUBLIC_ROUTES.copy()

def add_public_route(path: str) -> None:
    """Add a route to the public routes set (exceptions to authentication)."""
    PUBLIC_ROUTES.add(path)

def remove_public_route(path: str) -> None:
    """Remove a route from the public routes set (will make it protected)."""
    PUBLIC_ROUTES.discard(path)
