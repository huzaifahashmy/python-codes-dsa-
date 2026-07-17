import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# ----------------------------
# Shoelace Formula
# ----------------------------
def shoelace_area(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    return 0.5 * abs(
        np.dot(x, np.roll(y, -1))
        - np.dot(y, np.roll(x, -1))
    )


# ----------------------------
# Global Variables
# ----------------------------
points = []
polygon_patch = None
text_box = None
finished = False

# ----------------------------
# Create Figure
# ----------------------------
fig, ax = plt.subplots(figsize=(8, 8))

ax.set_title(
    "Click to add points\n"
    "Press ENTER to finish polygon\n"
    "Press R to Reset",
    fontsize=14
)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.set_aspect('equal')


# ----------------------------
# Mouse Click Event
# ----------------------------
def onclick(event):
    global finished

    if event.inaxes != ax:
        return

    if finished:
        return

    x = event.xdata
    y = event.ydata

    points.append((x, y))

    # Draw point
    ax.plot(x, y, 'ro', markersize=8)

    # Label point
    ax.text(x + 0.15, y + 0.15, str(len(points)), fontsize=10)

    # Draw line to previous point
    if len(points) > 1:
        x1, y1 = points[-2]
        x2, y2 = points[-1]
        ax.plot([x1, x2], [y1, y2], 'b-')

    fig.canvas.draw()


# ----------------------------
# Keyboard Events
# ----------------------------
def onkey(event):
    global polygon_patch, text_box, finished

    # ------------------------
    # Finish Polygon
    # ------------------------
    if event.key == "enter":

        if finished:
            return

        if len(points) < 3:
            print("Need at least 3 points.")
            return

        finished = True

        xs = [p[0] for p in points] + [points[0][0]]
        ys = [p[1] for p in points] + [points[0][1]]

        # Close polygon
        ax.plot(xs, ys, 'b-', linewidth=2)

        polygon_patch = Polygon(
            points,
            closed=True,
            facecolor="cyan",
            edgecolor="blue",
            alpha=0.35
        )

        ax.add_patch(polygon_patch)

        area = shoelace_area(points)

        centroid_x = np.mean([p[0] for p in points])
        centroid_y = np.mean([p[1] for p in points])

        text_box = ax.text(
            centroid_x,
            centroid_y,
            f"Area = {area:.4f} mm^2",
            fontsize=12,
            bbox=dict(facecolor="yellow", alpha=0.8)
        )

        print("\nSelected Points:")
        for i, p in enumerate(points, 1):
            print(f"P{i} = ({p[0]:.3f}, {p[1]:.3f})")

        print(f"\nShoelace Area = {area:.6f}")

        fig.canvas.draw()

    # ------------------------
    # Reset
    # ------------------------
    elif event.key.lower() == 'r':

        points.clear()
        finished = False

        ax.cla()

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.grid(True)
        ax.set_aspect('equal')

        ax.set_title(
            "Click to add points\n"
            "Press ENTER to finish polygon\n"
            "Press R to Reset",
            fontsize=14
        )

        polygon_patch = None
        text_box = None

        fig.canvas.draw()


# ----------------------------
# Connect Events
# ----------------------------
fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkey)

plt.show()