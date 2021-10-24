from graph import Graph


def main():
    facebook_users = Graph()
    for user in ["Bob", "Anne", "Elisa", "Diana", "Carl"]:
        facebook_users.add_vertex(user)

    facebook_users.add_edge("Carl", "Bob")
    facebook_users.add_edge("Carl", "Elisa")
    facebook_users.add_edge("Carl", "Diana")
    facebook_users.add_edge("Diana", "Bob")
    facebook_users.add_edge("Diana", "Anne")
    facebook_users.add_edge("Elisa", "Anne")
    facebook_users.add_edge("Anne", "Bob")
    print(facebook_users)
    print("\n")
    breadth_first_search(facebook_users, "Carl", "Anne")


main()