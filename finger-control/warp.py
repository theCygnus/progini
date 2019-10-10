from transform import four_point_transform

# Usage:
# pass arguments "image" and "pts" to function
#
# 	e.g.
# 	image = cv2.imread(image_file_path)
#	list_of_tuples = [(73, 239), (356, 117), (475, 265), (187, 443)]    # calculated points from
# 	pts = np.array(list_of_tuples, dtype = "float32")
#


def warp_image(image, pts):
    # apply the four point tranform to obtain a "birds eye view" of
    # the image
    warped = four_point_transform(image, pts)

    # show the original and warped images
    # cv2.imshow("Original", image)
    # cv2.imshow("Warped", warped)
    # cv2.waitKey(0)
