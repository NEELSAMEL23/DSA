def min_vans_required(n, k, weights):
    weights.sort()  # Sort the weights to optimize pairing
    left, right = 0, n - 1
    vans = 0

    while left <= right:
        if left == right:  # Only one parcel left
            vans += 1
            break

        if weights[left] + weights[right] <= k:
            left += 1  # Pair the lightest with the heaviest

        right -= 1  # Always move the right pointer (heavy parcel taken alone if not paired)
        vans += 1  # One van used

    return vans
