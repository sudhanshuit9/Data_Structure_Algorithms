def activity_selection(activities):
    # Sort activities based on their finish times
    activities.sort(key=lambda x: x[1])

    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities

# Example
activities = [(1, 3), (2, 5), (0, 6), (8, 9), (5, 7), (5, 9)]
result = activity_selection(activities)
print("Selected Activities:", result)
