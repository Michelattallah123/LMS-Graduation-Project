import React from "react";
import { connect } from "react-redux";

import { mapStateToProps, mapDispatchToProps } from "../../../store/reduxMaps";

const Notif = (props) => {
  const Notif  = [];

  console.log(props);

  props.recentUserPosts.userRecentPosts.forEach(
    (value)=> Notif.push(
      <h2>{value.Name} has Posted in {value.Location}</h2>
    )
  )

  return (
    <React.Fragment>
      {Notif}
    </React.Fragment>
  );
};

export default connect(mapStateToProps,mapDispatchToProps)(Notif);
